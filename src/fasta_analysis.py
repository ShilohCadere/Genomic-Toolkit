# src/fasta_analysis.py

from collections import Counter

class FASTAAnalyzer:
    def __init__(self, sequence: str):
        self.sequence = sequence.upper().replace("\n", "").replace("\r", "")

    def nucleotide_composition(self):
        counts = Counter(self.sequence)
        return {
            "A": counts.get("A", 0),
            "T": counts.get("T", 0),
            "G": counts.get("G", 0),
            "C": counts.get("C", 0),
            "N": counts.get("N", 0)
        }

    def gc_content(self):
        g = self.sequence.count("G")
        c = self.sequence.count("C")
        return (g + c) / len(self.sequence) * 100

    def at_content(self):
        a = self.sequence.count("A")
        t = self.sequence.count("T")
        return (a + t) / len(self.sequence) * 100

    def reverse_complement(self):
        complement = str.maketrans("ATCG", "TAGC")
        return self.sequence.translate(complement)[::-1]
