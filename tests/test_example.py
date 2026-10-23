import unittest
from pathlib import Path
from genomic_toolkit.fasta_analysis import FASTAAnalyzer
from genomic_toolkit.sequence_translation import SequenceTranslator

ROOT = Path(__file__).resolve().parents[1]

class GenomicToolkitTests(unittest.TestCase):
    def test_bundled_fasta_metrics_and_translation(self):
        lines = (ROOT / "data" / "sequence.fasta").read_text().splitlines()
        self.assertTrue(lines[0].startswith(">"))
        seq = "".join(lines[1:]).strip()
        self.assertEqual(len(seq), 70)
        self.assertTrue(set(seq) <= set("ATGCN"))
        a = FASTAAnalyzer(seq)
        self.assertEqual(a.nucleotide_composition(), {"A":18,"T":20,"G":21,"C":11,"N":0})
        self.assertAlmostEqual(a.gc_content(), 45.7142857143)
        self.assertAlmostEqual(a.at_content(), 54.2857142857)
        self.assertEqual(SequenceTranslator(seq).translate_frame(1), "EQE_RAKRMAPKGLIFLAVLCFS")

    def test_reverse_complement_and_translation(self):
        self.assertEqual(FASTAAnalyzer("ATGC").reverse_complement(), "GCAT")
        self.assertEqual(SequenceTranslator("ATGGAATAG").translate_frame(1), "ME_")

if __name__ == "__main__":
    unittest.main()
