"""Test SPARQL Implementation."""
import logging
import shutil
import unittest

from oaklib.datamodels import obograph
from oaklib.datamodels.search import SearchConfiguration
from oaklib.datamodels.search_datamodel import SearchProperty, SearchTermSyntax
from oaklib.datamodels.vocabulary import IS_A, PART_OF
from oaklib.implementations.sparql.sparql_implementation import SparqlImplementation
from oaklib.resource import OntologyResource
from oaklib.utilities.obograph_utils import (
    graph_as_dict,
    index_graph_edges_by_object,
    index_graph_edges_by_predicate,
    index_graph_edges_by_subject,
    index_graph_nodes,
)
from tests import (
    CATALYTIC_ACTIVITY,
    CELL_CORTEX,
    CELLULAR_COMPONENT,
    CYTOPLASM,
    DIGIT,
    FAKE_ID,
    FAKE_PREDICATE,
    INPUT_DIR,
    NUCLEAR_ENVELOPE,
    NUCLEUS,
    OUTPUT_DIR,
    SHAPE,
    VACUOLE,
)

TEST_RDF = INPUT_DIR / "go-nucleus.owl.ttl"
TEST_MUTABLE_RDF = OUTPUT_DIR / "go-nucleus.owl.ttl"


class TestSparqlImplementation(unittest.TestCase):
    """Test SPARQL Implementation."""

    def setUp(self) -> None:
        """Set up."""
        oi = SparqlImplementation(OntologyResource(slug=str(TEST_RDF)))
        self.oi = oi

    def test_relationships(self):
        """Test relationships."""
        oi = self.oi
        self.assertIsNotNone(oi.graph)
        rels = oi.get_outgoing_relationship_map_by_curie(VACUOLE)
        for k, v in rels.items():
            logging.info(f"{k} = {v}")
        self.assertIn("GO:0043231", rels[IS_A])
        self.assertIn("GO:0005737", rels[PART_OF])

    def test_parents(self):
        """Test parents."""
        parents = self.oi.get_hierararchical_parents_by_curie(VACUOLE)
        # print(parents)
        assert "GO:0043231" in parents

    def test_labels(self):
        """Test labels."""
        label = self.oi.get_label_by_curie(NUCLEUS)
        logging.info(label)
        self.assertEqual(label, "nucleus")
        self.assertEqual(self.oi.get_curies_by_label(label), [NUCLEUS])

    @unittest.skip("TODO")
    def test_subontology(self):
        """Test subontology."""
        oi = self.oi
        self.assertIsNotNone(oi.named_graph)
        label = oi.get_label_by_curie(DIGIT)
        self.assertIsNone(label)
        # logging.info(label)
        # self.assertEqual(label, 'digit')
        self.assertEqual("shape", oi.get_label_by_curie(SHAPE))

    def test_dump(self):
        """Test dump."""
        OUTPUT_DIR.mkdir(exist_ok=True)
        self.oi.dump(TEST_MUTABLE_RDF, "ttl")

    @unittest.skip("TODO")
    def test_set_label(self):
        """Test set label."""
        self.oi.set_label_for_curie(NUCLEUS, "foo")
        OUTPUT_DIR.mkdir(exist_ok=True)
        self.oi.dump(TEST_MUTABLE_RDF, "ttl")

    def test_synonyms(self):
        """Test synonyms."""
        syns = self.oi.aliases_by_curie(CELLULAR_COMPONENT)
        logging.info(syns)
        assert "cellular component" in syns
        assert "cellular_component" in syns
        syns = self.oi.aliases_by_curie(NUCLEUS)
        logging.info(syns)
        self.assertCountEqual(syns, ["nucleus", "cell nucleus", "horsetail nucleus"])
        syn_pairs = list(self.oi.alias_map_by_curie(NUCLEUS).items())
        self.assertCountEqual(
            syn_pairs,
            [
                ("oio:hasExactSynonym", ["cell nucleus"]),
                ("oio:hasNarrowSynonym", ["horsetail nucleus"]),
                ("rdfs:label", ["nucleus"]),
            ],
        )

    def test_all_entity_curies(self):
        """Test all entity curies."""
        curies = list(self.oi.all_entity_curies())
        self.assertGreater(len(curies), 100)
        self.assertIn(NUCLEUS, curies)

    def test_definition(self):
        """Test definition."""
        defn = self.oi.get_definition_by_curie(CELLULAR_COMPONENT)
        assert defn.startswith("A location, relative to cellular compartments")

    def test_search_exact(self):
        """Test search exact."""
        config = SearchConfiguration(is_partial=False)
        curies = list(self.oi.basic_search("nucleus", config=config))
        # print(curies)
        assert NUCLEUS in curies
        config = SearchConfiguration(is_partial=False, properties=[SearchProperty.LABEL])
        curies = list(self.oi.basic_search("nucleus", config=config))
        assert NUCLEUS in curies
        curies = list(self.oi.basic_search("enzyme activity", config=config))
        assert curies == []
        config = SearchConfiguration(is_partial=False, properties=[SearchProperty.ALIAS])
        curies = list(self.oi.basic_search("enzyme activity", config=config))
        assert CATALYTIC_ACTIVITY in curies

    def test_search_partial(self):
        """Test partial."""
        config = SearchConfiguration(is_partial=True)
        # non-exact matches across all ontobee are slow: restrict to pato
        curies = list(self.oi.basic_search("ucl", config=config))
        # print(curies)
        self.assertGreater(len(curies), 1)
        assert NUCLEUS in curies

    def test_obograph(self):
        """Test Obograph."""
        g = self.oi.ancestor_graph(VACUOLE)
        nix = index_graph_nodes(g)
        self.assertEqual(nix[VACUOLE].lbl, "vacuole")
        v2c = obograph.Edge(sub=VACUOLE, pred=PART_OF, obj=CYTOPLASM)
        six = index_graph_edges_by_subject(g)
        self.assertIn(v2c, six[VACUOLE])
        self.assertNotIn(v2c, six[CYTOPLASM])
        oix = index_graph_edges_by_object(g)
        self.assertIn(v2c, oix[CYTOPLASM])
        self.assertNotIn(v2c, oix[VACUOLE])
        pix = index_graph_edges_by_predicate(g)
        self.assertIn(v2c, pix[PART_OF])
        self.assertNotIn(v2c, pix[IS_A])
        graph_as_dict(g)
        assert "nodes" in g
        assert "edges" in g
        # check is reflexive
        self.assertEqual(1, len([n for n in g.nodes if n.id == VACUOLE]))
        ancs = list(self.oi.ancestors(VACUOLE, predicates=[IS_A, PART_OF]))
        assert VACUOLE in ancs
        assert CYTOPLASM in ancs

    def test_descendants(self):
        """Test descendants."""
        descs = list(self.oi.descendants(CYTOPLASM, predicates=[IS_A, PART_OF]))
        self.assertIn(VACUOLE, descs)
        self.assertIn(CYTOPLASM, descs)
        self.assertIn(CELL_CORTEX, descs)
        for desc in descs:
            self.assertIn(CYTOPLASM, list(self.oi.ancestors(desc, predicates=[IS_A, PART_OF])))
        descs = list(self.oi.descendants(CYTOPLASM, predicates=[PART_OF]))
        self.assertIn(VACUOLE, descs)
        self.assertIn(CYTOPLASM, descs)
        self.assertNotIn(CELL_CORTEX, descs)
        descs = list(self.oi.descendants(CYTOPLASM, predicates=[IS_A]))
        self.assertNotIn(VACUOLE, descs)
        self.assertIn(CYTOPLASM, descs)
        self.assertIn(CELL_CORTEX, descs)
        self.assertEqual([NUCLEUS], list(self.oi.descendants(NUCLEUS, predicates=[IS_A])))

    def test_search_starts_with(self):
        """Test 'search starts with' feature."""
        config = SearchConfiguration(syntax=SearchTermSyntax.STARTS_WITH)
        curies = list(self.oi.basic_search("nucl", config=config))
        # print(curies)
        # self.assertGreater(len(curie), 1)
        assert NUCLEUS in curies

    def test_search_regex(self):
        """Test search regex."""
        config = SearchConfiguration(syntax=SearchTermSyntax.REGULAR_EXPRESSION)
        curies = list(self.oi.basic_search("nucl.* envelope$", config=config))
        print(curies)
        # self.assertGreater(len(curie), 1)
        assert NUCLEAR_ENVELOPE in curies

    def test_mutable(self):
        """
        Tests the SPARQL store can be modified.

        Currently only tests
        """
        shutil.copyfile(TEST_RDF, TEST_MUTABLE_RDF)
        oi = SparqlImplementation(OntologyResource(slug=str(TEST_MUTABLE_RDF)))
        label = oi.get_label_by_curie(NUCLEUS)
        preds = [IS_A, PART_OF]
        preds2 = [IS_A, FAKE_PREDICATE]
        ancestors = list(oi.ancestors(NUCLEUS, predicates=preds, reflexive=False))
        descendants = list(oi.descendants(NUCLEUS, predicates=preds, reflexive=False))
        oi.migrate_curies({NUCLEUS: FAKE_ID, PART_OF: FAKE_PREDICATE})
        self.assertEqual(label, oi.get_label_by_curie(FAKE_ID))
        self.assertIsNone(oi.get_label_by_curie(NUCLEUS))
        self.assertCountEqual(ancestors, oi.ancestors(FAKE_ID, predicates=preds2, reflexive=False))
        self.assertCountEqual([], list(oi.ancestors(NUCLEUS, predicates=preds, reflexive=False)))
        self.assertCountEqual(
            descendants, oi.descendants(FAKE_ID, predicates=preds2, reflexive=False)
        )
        self.assertCountEqual([], list(oi.descendants(NUCLEUS, predicates=preds, reflexive=False)))
        oi.save()
