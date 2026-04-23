import argparse
from src.fasta_analysis import FASTAAnalyzer
from src.sequence_translation import SequenceTranslator


def load_fasta(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    return "".join(lines[1:])


def main():
    parser = argparse.ArgumentParser(
        description="Modular Genomic Sequence Analysis Toolkit"
    )

    parser.add_argument("--file", required=True,
                        help="Path to FASTA file (e.g., data/sequence.fasta)")

    parser.add_argument("--gc", action="store_true",
                        help="Calculate GC content")

    parser.add_argument("--at", action="store_true",
                        help="Calculate AT content")

    parser.add_argument("--composition", action="store_true",
                        help="Show nucleotide composition")

    parser.add_argument("--translate", type=int, choices=[1, 2, 3],
                        help="Translate sequence in reading frame (1-3)")

    parser.add_argument("--out",
                        help="Output file to save results")

    args = parser.parse_args()

    sequence = load_fasta(args.file)

    analyzer = FASTAAnalyzer(sequence)
    translator = SequenceTranslator(sequence)

    results = []

    if args.composition:
        result = f"Nucleotide Composition: {analyzer.nucleotide_composition()}"
        print(result)
        results.append(result)

    if args.gc:
        result = f"GC content: {analyzer.gc_content():.2f}%"
        print(result)
        results.append(result)

    if args.at:
        result = f"AT content: {analyzer.at_content():.2f}%"
        print(result)
        results.append(result)

    if args.translate:
        protein = translator.translate_frame(args.translate)
        result = f"Translation (frame {args.translate}):\n{protein}"
        print(result)
        results.append(result)

    if args.out:
        with open(args.out, "w") as f:
            f.write("\n".join(results))


if __name__ == "__main__":
    main()