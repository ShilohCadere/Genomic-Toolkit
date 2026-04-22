# src/cli.py

import argparse
from fasta_analysis import FASTAAnalyzer
from sequence_translation import SequenceTranslator


def load_fasta(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    return "".join(lines[1:])  # skip FASTA header


def main():
    parser = argparse.ArgumentParser(
        description="Modular Genomic Sequence Analysis Toolkit"
    )

    parser.add_argument(
        "--file",
        required=True,
        help="Path to FASTA file (e.g., data/sequence.fasta)"
    )

    parser.add_argument(
        "--gc",
        action="store_true",
        help="Calculate GC content"
    )

    parser.add_argument(
        "--at",
        action="store_true",
        help="Calculate AT content"
    )

    parser.add_argument(
        "--composition",
        action="store_true",
        help="Show nucleotide composition"
    )

    parser.add_argument(
        "--translate",
        type=int,
        choices=[1, 2, 3],
        help="Translate sequence in reading frame (1-3)"
    )

    args = parser.parse_args()

    sequence = load_fasta(args.file)

    analyzer = FASTAAnalyzer(sequence)
    translator = SequenceTranslator(sequence)

    if args.composition:
        print(analyzer.nucleotide_composition())

    if args.gc:
        print(f"GC content: {analyzer.gc_content():.2f}%")

    if args.at:
        print(f"AT content: {analyzer.at_content():.2f}%")

    if args.translate:
        print(translator.translate_frame(args.translate))


if __name__ == "__main__":
    main()
