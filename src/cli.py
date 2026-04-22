# src/cli.py

from fasta_analysis import FASTAAnalyzer
from sequence_translation import SequenceTranslator

def load_fasta(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    return "".join(lines[1:])  # skip header

def main():
    file_path = input("Enter FASTA file path (data/sequence.fasta): ")
    sequence = load_fasta(file_path)

    analyzer = FASTAAnalyzer(sequence)
    translator = SequenceTranslator(sequence)

    print("\nChoose option:")
    print("1. Nucleotide composition")
    print("2. GC content")
    print("3. Translate frame 1")

    choice = input("> ")

    if choice == "1":
        print(analyzer.nucleotide_composition())

    elif choice == "2":
        print(analyzer.gc_content())

    elif choice == "3":
        print(translator.translate_frame(1))

if __name__ == "__main__":
    main()
