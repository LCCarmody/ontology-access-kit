import inspect
import logging
import math
import pickle
import statistics
from collections import defaultdict
from dataclasses import dataclass, field
from typing import ClassVar, List, Iterable, Dict, Iterator, Union, Tuple

from oaklib.constants import OAKLIB_MODULE
from oaklib.datamodels import obograph, ontology_metadata
from oaklib.datamodels.association import Association
from oaklib.datamodels.obograph import (
    ExistentialRestrictionExpression,
    LogicalDefinitionAxiom,
)
from oaklib.datamodels.search import SearchConfiguration
from oaklib.datamodels.search_datamodel import SearchProperty, SearchTermSyntax
from oaklib.datamodels.similarity import TermPairwiseSimilarity, TermSetPairwiseSimilarity, TermInfo, BestMatch
from oaklib.datamodels.vocabulary import (
    ALL_MATCH_PREDICATES,
    DEPRECATED_PREDICATE,
    DISJOINT_WITH,
    EQUIVALENT_CLASS,
    HAS_DBXREF,
    HAS_EXACT_SYNONYM,
    HAS_SYNONYM_TYPE,
    IN_CATEGORY_PREDS,
    IN_SUBSET,
    IS_A,
    LABEL_PREDICATE,
    OWL_NOTHING,
    OWL_THING,
    RDF_TYPE,
    SEMAPV,
    SYNONYM_PREDICATES,
    omd_slots, PART_OF,
)
from oaklib.implementations.bitwise.bitwise_ontology_index import BitwiseOntologyIndex
from oaklib.implementations.bitwise.bitwise_utils import bitmap_from_list, BITMAP, POS, map_bitmap_to_ints, \
    bitmap_cardinality
from oaklib.implementations.sqldb import SEARCH_CONFIG
from oaklib.interfaces import SubsetterInterface, TextAnnotatorInterface
from oaklib.interfaces.association_provider_interface import (
    AssociationProviderInterface,
)
from oaklib.interfaces.basic_ontology_interface import (
    ALIAS_MAP,
    METADATA_MAP,
    PRED_CURIE,
    PREFIX_MAP,
    RELATIONSHIP,
    RELATIONSHIP_MAP,
    BasicOntologyInterface,
)
from oaklib.interfaces.differ_interface import DifferInterface
from oaklib.interfaces.mapping_provider_interface import MappingProviderInterface
from oaklib.interfaces.metadata_interface import MetadataInterface
from oaklib.interfaces.obograph_interface import OboGraphInterface
from oaklib.interfaces.patcher_interface import PatcherInterface
from oaklib.interfaces.relation_graph_interface import RelationGraphInterface
from oaklib.interfaces.search_interface import SearchInterface
from oaklib.interfaces.semsim_interface import SemanticSimilarityInterface
from oaklib.interfaces.validator_interface import ValidatorInterface
from oaklib.types import CATEGORY_CURIE, CURIE, SUBSET_CURIE
from oaklib.utilities.basic_utils import get_curie_prefix, pairs_as_dict




@dataclass
class BitwiseImplementation(
    RelationGraphInterface,
    OboGraphInterface,
    ValidatorInterface,
    SearchInterface,
    SubsetterInterface,
    MappingProviderInterface,
    PatcherInterface,
    SemanticSimilarityInterface,
    MetadataInterface,
    DifferInterface,
    AssociationProviderInterface,
    TextAnnotatorInterface,
):
    wrapped_adapter: OboGraphInterface = None
    """An OAK implementation that takes care of everything that ensmallen cannot handle"""

    closure_predicates: List[PRED_CURIE] = field(default_factory=lambda: [IS_A, PART_OF])

    jaccard_threshold: float = field(default=0.5)

    ontology_index: BitwiseOntologyIndex = None

    delegated_methods: ClassVar[List[str]] = [
        BasicOntologyInterface.entities,
        BasicOntologyInterface.label,
        BasicOntologyInterface.labels,
        BasicOntologyInterface.curie_to_uri,
        BasicOntologyInterface.uri_to_curie,
        BasicOntologyInterface.ontologies,
        BasicOntologyInterface.obsoletes,
        SearchInterface.basic_search,
        OboGraphInterface.node,
    ]
    """all methods that should be delegated to wrapped_adapter"""

    def __post_init__(self):
        if self.wrapped_adapter is None:
            from oaklib.selector import get_implementation_from_shorthand

            slug = self.resource.slug
            logging.info(f"Wrapping an existing OAK implementation to fetch {slug}")
            inner_oi = get_implementation_from_shorthand(slug)
            self.wrapped_adapter = inner_oi
        # delegation magic
        methods = dict(inspect.getmembers(self.wrapped_adapter))
        for m in self.delegated_methods:
            mn = m if isinstance(m, str) else m.__name__
            setattr(BitwiseImplementation, mn, methods[mn])
        self.build_index()

    def build_index(self):
        self.ontology_index = BitwiseOntologyIndex()
        self.build_curie_index()
        self.build_ancestor_index()
        self.build_information_content_index()
        self.build_term_pair_index()

    def build_curie_index(self):
        logging.info("Building curie index")
        oix = self.ontology_index
        n = 0
        _curie_to_int = {}
        _int_to_curie = {}
        for e in self.wrapped_adapter.entities():
            _curie_to_int[e] = n
            _int_to_curie[n] = e
            n += 1
        oix.curie_to_int = _curie_to_int
        oix.int_to_curie = _int_to_curie

    def build_ancestor_index(self):
        logging.info("Building ancestor index")
        oix = self.ontology_index
        oix.ancestor_map = {}
        oix.ancestors_map_bitmap = {}
        inner_oi = self.wrapped_adapter
        for i, e in oix.int_to_curie.items():
            ancs = inner_oi.ancestors(e, predicates=self.closure_predicates, reflexive=True)
            oix.ancestor_map[i] = self._map_curies_to_ints(ancs)
            oix.ancestors_map_bitmap[i] = bitmap_from_list(oix.ancestor_map[i])

    def build_association_index(self):
        logging.info("Building association index")
        oix = self.ontology_index
        _curie_to_int = oix.curie_to_int
        obj_closure_bm: Dict[POS, BITMAP] = defaultdict(BITMAP)
        for a in self.associations():
            s_ix = _curie_to_int[a.subject]
            bm = oix.ancestors_map_bitmap[_curie_to_int[a.object]]
            obj_closure_bm[s_ix] |= bm

    def build_information_content_index(self):
        logging.info("Building information content index")
        oix = self.ontology_index
        oix.information_content_map = {}
        counts = defaultdict(int)
        if self._association_index:
            raise NotImplementedError
        else:
            for i, e in oix.int_to_curie.items():
                ancs = self.ontology_index.ancestor_map[i]
                for a in ancs:
                    counts[a] += 1
            for i, count in counts.items():
                oix.information_content_map[i] = -math.log(count / len(oix.int_to_curie))/math.log(2)

    def build_term_pair_index(self):
        logging.info("Building term pair index")
        oix = self.ontology_index
        oix.term_pair_jaccard_index = {}
        oix.term_pair_max_information_content = {}
        oix.term_pair_best_ancestor = {}
        entities = self.filtered_entities()
        entity_ixs = [oix.curie_to_int[e] for e in entities]
        for e1_ix in entity_ixs:
            #e1_ix = oix.curie_to_int[e1]
            logging.info(f"Indexing {e1_ix}")
            anc_bm1 = oix.ancestors_map_bitmap[e1_ix]
            for e2_ix in entity_ixs:
                #e2_ix = oix.curie_to_int[e2]
                anc_bm2 = oix.ancestors_map_bitmap[e2_ix]
                if e1_ix <= e2_ix:
                    anc_intersection = anc_bm1 & anc_bm2
                    anc_union = anc_bm1 | anc_bm2
                    if not anc_union:
                        # TODO
                        continue
                    jaccard = bitmap_cardinality(anc_intersection) / bitmap_cardinality(anc_union)
                    if jaccard > self.jaccard_threshold:
                        oix.term_pair_jaccard_index[(e1_ix, e2_ix)] = jaccard
                        anc_ints = map_bitmap_to_ints(anc_intersection)
                        ics = [oix.information_content_map[i] for i in anc_ints]
                        max_ics = max(ics)
                        oix.term_pair_max_information_content[(e1_ix, e2_ix)] = max_ics
                        best_ancs = [i for i in anc_ints if math.isclose(oix.information_content_map[i], max_ics, rel_tol=1e-5)]
                        oix.term_pair_best_ancestor[(e1_ix, e2_ix)] = best_ancs

    def _jaccard_using_ints(self, e1_ix: POS, e2_ix: POS, anc_bm1: BITMAP = None) -> float:
        oix = self.ontology_index
        if anc_bm1 is None:
            anc_bm1 = oix.ancestors_map_bitmap[e1_ix]
        anc_bm2 = oix.ancestors_map_bitmap[e2_ix]
        anc_intersection = anc_bm1 & anc_bm2
        anc_union = anc_bm1 | anc_bm2
        return bitmap_cardinality(anc_intersection) / bitmap_cardinality(anc_union)

    def filtered_entities(self) -> List[CURIE]:
        return list(self.entities())

    def dump(self, path: str = None, syntax: str = None):
        protocol = 0
        if syntax is not None:
            if "." in syntax:
                protocol = int(syntax.split(".")[-1])
        logging.info("Duping index")
        with open(path, "wb") as file:
            pickle.dump(self.ontology_index, file, protocol=protocol)

    def _map_curies_to_ints(self, curies: Iterable[CURIE]) -> Iterator[POS]:
        oix = self.ontology_index
        return [oix.curie_to_int[c] for c in curies]

    def _map_ints_to_curies(self, ints: Iterable[POS]) -> Iterator[CURIE]:
        oix = self.ontology_index
        return [oix.int_to_curie[i] for i in ints]

    def _map_bitmap_to_curies(self, bm: BITMAP) -> Iterator[CURIE]:
        oix = self.ontology_index
        ints = map_bitmap_to_ints(bm)
        return [oix.int_to_curie[i] for i in ints]

    def ancestors(
        self,
        start_curies: Union[CURIE, List[CURIE]],
        predicates: List[PRED_CURIE] = None,
        reflexive=True,
    ) -> Iterable[CURIE]:
        if isinstance(start_curies, str):
            start_curies = [start_curies]
        oix = self.ontology_index
        bm = 0
        for e in start_curies:
            bm |= oix.ancestors_map_bitmap[oix.curie_to_int[e]]
        return self._map_bitmap_to_curies(bm)

    def information_content_scores(
            self,
            curies: Iterable[CURIE],
            predicates: List[PRED_CURIE] = None,
            object_closure_predicates: List[PRED_CURIE] = None,
            use_associations: bool = None,
    ) -> Iterator[Tuple[CURIE, float]]:
        oix = self.ontology_index
        for c in curies:
            if c in oix.curie_to_int:
                c_ix = oix.curie_to_int[c]
                if c_ix in oix.information_content_map:
                    yield c, oix.information_content_map[c_ix]
                else:
                    # TODO
                    yield c, 0.0
            else:
                yield c, 0.0

    def pairwise_similarity(
            self,
            subject: CURIE,
            object: CURIE,
            predicates: List[PRED_CURIE] = None,
            subject_ancestors: List[CURIE] = None,
            object_ancestors: List[CURIE] = None,
    ) -> TermPairwiseSimilarity:
        oix = self.ontology_index
        s_ix = oix.curie_to_int[subject]
        o_ix = oix.curie_to_int[object]
        k = (s_ix, o_ix)
        if k not in oix.term_pair_jaccard_index:
            k = (o_ix, s_ix)
        if k in oix.term_pair_jaccard_index:
            jaccard = oix.term_pair_jaccard_index[k]
            return TermPairwiseSimilarity(
                subject_id=subject,
                object_id=object,
                jaccard_similarity=jaccard,
                ancestor_information_content=oix.term_pair_max_information_content[k],
                ancestor_id=self._map_ints_to_curies(oix.term_pair_best_ancestor[k])[0],
            )
        else:
            return TermPairwiseSimilarity(
                subject_id=subject,
                object_id=object,
                jaccard_similarity=0,
                ancestor_information_content=0.0,
            )

    def _all_by_all_pairwise_similarity_on_indexes(
            self,
            subjects: Iterable[POS],
            objects: Iterable[POS],
    ) -> Iterator[Tuple]:
        objects = list(objects)
        for s in subjects:
            anc1_bm = self.ontology_index.ancestors_map_bitmap[s]
            for o in objects:
                yield s, o, self._jaccard_using_ints(s, o, anc1_bm)

    def termset_pairwise_similarity(
            self,
            subjects: List[CURIE],
            objects: List[CURIE],
            predicates: List[PRED_CURIE] = None,
            labels=False,
    ) -> TermSetPairwiseSimilarity:
        oix = self.ontology_index
        subject_ixs = self._map_curies_to_ints(subjects)
        object_ixs = self._map_curies_to_ints(objects)
        pairs = list(self._all_by_all_pairwise_similarity_on_indexes(subject_ixs, object_ixs))
        bm_subject_score: Dict[POS, float] = defaultdict(float)
        bm_subject: Dict[POS, POS] = {}
        bm_subject_sim = {}
        bm_object_score: Dict[POS, float] = defaultdict(float)
        bm_object: Dict[POS, POS] = {}
        bm_object_sim = {}
        sim = TermSetPairwiseSimilarity()
        for x in subjects:
            sim.subject_termset[x] = TermInfo(x)
        for x in objects:
            sim.object_termset[x] = TermInfo(x)
        for s_ix, o_ix, j_score in pairs:
            if j_score > bm_subject_score[s_ix]:
                bm_subject_score[s_ix] = j_score
                bm_subject[s_ix] = o_ix
                bm_subject_sim[s_ix] = j_score
            if j_score > bm_object_score[o_ix]:
                bm_object_score[o_ix] = j_score
                bm_object[o_ix] = s_ix
                bm_object_sim[o_ix] = j_score
        scores = []
        for s_ix, t_ix in bm_subject.items():
            s = oix.int_to_curie[s_ix]
            score = bm_subject_score[s_ix]
            sim.subject_best_matches[s] = BestMatch(
                s, match_target=oix.int_to_curie[t_ix], score=score,
            )
            scores.append(score)
        for s_ix, t_ix in bm_object.items():
            s = oix.int_to_curie[s_ix]
            score = bm_object_score[s_ix]
            sim.object_best_matches[s] = BestMatch(
                s, match_target=oix.int_to_curie[t_ix], score=score,
            )
            scores.append(score)
        if not scores:
            scores = [0.0]
        sim.average_score = statistics.mean(scores)
        sim.best_score = max(scores)
        return sim

