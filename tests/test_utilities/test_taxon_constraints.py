import logging
import unittest

from linkml_runtime.dumpers import yaml_dumper
from oaklib.implementations.pronto.pronto_implementation import ProntoImplementation
from oaklib.implementations.sqldb.sql_implementation import SqlImplementation
from oaklib.resource import OntologyResource
from oaklib.datamodels.vocabulary import IS_A, PART_OF
from oaklib.utilities.subsets.slimmer_utils import roll_up_to_named_subset
from oaklib.utilities.subsets.subset_analysis import all_subsets_overlap, compare_all_subsets, terms_by_subsets
from oaklib.utilities.taxon.taxon_constraint_utils import nr_term_taxon_constraints_simple, all_term_taxon_constraints, \
    get_term_with_taxon_constraints

from tests import OUTPUT_DIR, INPUT_DIR, INTRACELLULAR, CELLULAR_ORGANISMS, PHOTOSYNTHETIC_MEMBRANE, \
    PLANTS_OR_CYANOBACTERIA
from tests.test_cli import NUCLEUS, NUCLEAR_ENVELOPE, BACTERIA, EUKARYOTA

DB = INPUT_DIR / 'go-nucleus.db'
TEST_ONT = INPUT_DIR / 'go-nucleus.obo'
TEST_OUT = OUTPUT_DIR / 'go-nucleus.saved.owl'

PREDS = [IS_A, PART_OF]

class TestTaxonConstraintsUtils(unittest.TestCase):

    def setUp(self) -> None:
        oi = ProntoImplementation(OntologyResource(slug=str(TEST_ONT), local=True))
        self.oi = oi

    def test_never_in(self):
        oi = self.oi
        never, only = all_term_taxon_constraints(oi, NUCLEUS)
        self.assertCountEqual([BACTERIA], never)
        never, only = all_term_taxon_constraints(oi, NUCLEAR_ENVELOPE)
        self.assertCountEqual([BACTERIA], never)
        never, only = all_term_taxon_constraints(oi, NUCLEAR_ENVELOPE, predicates=[IS_A])
        self.assertCountEqual([], never)
        st = get_term_with_taxon_constraints(oi, NUCLEAR_ENVELOPE, include_redundant=True)
        [never] = [tc for tc in st.never_in if not tc.redundant]
        assert never.redundant_with_only_in
        [only] = [tc for tc in st.only_in if not tc.redundant]
        assert not only.redundant_with_only_in
        assert only.taxon.id == EUKARYOTA
        assert only.redundant_with == []
        # See: https://github.com/althonos/pronto/issues/163


    def test_intracellular(self):
        oi = self.oi
        t = INTRACELLULAR
        st = get_term_with_taxon_constraints(oi, t, include_redundant=True)
        self.assertCountEqual(st.never_in, [])
        self.assertEqual(1, len(st.only_in))
        never = [tc.taxon.id for tc in st.never_in]
        only = [tc.taxon.id for tc in st.only_in]
        never_nr = [tc.taxon.id for tc in st.never_in if not tc.redundant]
        only_nr = [tc.taxon.id for tc in st.only_in if not tc.redundant]
        never_r = [tc.taxon.id for tc in st.never_in if tc.redundant]
        only_r = [tc.taxon.id for tc in st.only_in if tc.redundant]
        self.assertCountEqual([CELLULAR_ORGANISMS], only)
        self.assertCountEqual([CELLULAR_ORGANISMS], only_nr)
        self.assertCountEqual([], only_r)

    def test_photosynthetic_membrane(self):
        oi = self.oi
        t = PHOTOSYNTHETIC_MEMBRANE
        st = get_term_with_taxon_constraints(oi, t, include_redundant=True)
        print(yaml_dumper.dumps(st))
        self.assertCountEqual(st.never_in, [])
        self.assertEqual(2, len(st.only_in))
        never = [tc.taxon.id for tc in st.never_in]
        only = [tc.taxon.id for tc in st.only_in]
        never_nr = [tc.taxon.id for tc in st.never_in if not tc.redundant]
        only_nr = [tc.taxon.id for tc in st.only_in if not tc.redundant]
        never_r = [tc.taxon.id for tc in st.never_in if tc.redundant]
        only_r = [tc.taxon.id for tc in st.only_in if tc.redundant]
        self.assertCountEqual([PLANTS_OR_CYANOBACTERIA, CELLULAR_ORGANISMS], only)
        self.assertCountEqual([PLANTS_OR_CYANOBACTERIA], only_nr)
        self.assertCountEqual([CELLULAR_ORGANISMS], only_r)

    def test_nuclear_envelope(self):
        oi = self.oi
        t = NUCLEAR_ENVELOPE
        st = get_term_with_taxon_constraints(oi, t, include_redundant=True)
        print(yaml_dumper.dumps(st))
        self.assertEqual(1, len(st.never_in))
        self.assertEqual(2, len(st.only_in))
        never = [tc.taxon.id for tc in st.never_in]
        only = [tc.taxon.id for tc in st.only_in]
        never_nr = [tc.taxon.id for tc in st.never_in if not tc.redundant]
        only_nr = [tc.taxon.id for tc in st.only_in if not tc.redundant]
        never_r = [tc.taxon.id for tc in st.never_in if tc.redundant]
        only_r = [tc.taxon.id for tc in st.only_in if tc.redundant]
        self.assertCountEqual([BACTERIA], never)
        self.assertCountEqual([BACTERIA], never_nr)
        self.assertCountEqual([], never_r)
        assert st.never_in[0].redundant_with_only_in
        self.assertCountEqual([EUKARYOTA, CELLULAR_ORGANISMS], only)
        self.assertCountEqual([EUKARYOTA], only_nr)
        self.assertCountEqual([CELLULAR_ORGANISMS], only_r)


    def test_taxon_subclass(self):
        self.assertIn(CELLULAR_ORGANISMS, list(self.oi.ancestors(BACTERIA, predicates=[IS_A])))

    def test_all(self):
        oi = self.oi
        term_curies = [t for t in oi.all_entity_curies() if t.startswith('GO:')]
        for t in term_curies:
            never, only = all_term_taxon_constraints(oi, t)
            never_nr, only_nr = nr_term_taxon_constraints_simple(oi, t)