# src/sequence_translation.py

class SequenceTranslator:
    def __init__(self, sequence: str):
        self.sequence = sequence.upper().replace("\n", "").replace("\r", "")

    codon_table = {
        'ATA':'I','ATC':'I','ATT':'I','ATG':'M',
        'ACA':'T','ACC':'T','ACG':'T','ACT':'T',
        'AAC':'N','AAT':'N','AAA':'K','AAG':'K',
        'AGC':'S','AGT':'S','AGA':'R','AGG':'R',
        'CTA':'L','CTC':'L','CTG':'L','CTT':'L',
        'CCA':'P','CCC':'P','CCG':'P','CCT':'P',
        'CAC':'H','CAT':'H','CAA':'Q','CAG':'Q',
        'CGA':'R','CGC':'R','CGG':'R','CGT':'R',
        'GTA':'V','GTC':'V','GTG':'V','GTT':'V',
        'GCA':'A','GCC':'A','GCG':'A','GCT':'A',
        'GAC':'D','GAT':'D','GAA':'E','GAG':'E',
        'GGA':'G','GGC':'G','GGG':'G','GGT':'G',
        'TCA':'S','TCC':'S','TCG':'S','TCT':'S',
        'TTC':'F','TTT':'F','TTA':'L','TTG':'L',
        'TAC':'Y','TAT':'Y','TAA':'_','TAG':'_',
        'TGC':'C','TGT':'C','TGA':'_','TGG':'W'
    }

    def translate_frame(self, frame=1):
        start = frame - 1
        protein = []

        for i in range(start, len(self.sequence) - 2, 3):
            codon = self.sequence[i:i+3]
            protein.append(self.codon_table.get(codon, "X"))

        return "".join(protein)

    def reverse_translate_frame(self, frame=1):
        complement = str.maketrans("ATCG", "TAGC")
        rev_seq = self.sequence.translate(complement)[::-1]

        start = frame - 1
        protein = []

        for i in range(start, len(rev_seq) - 2, 3):
            codon = rev_seq[i:i+3]
            protein.append(self.codon_table.get(codon, "X"))

        return "".join(protein)
