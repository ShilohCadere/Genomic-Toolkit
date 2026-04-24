# Genomic Toolkit — CLI Bioinformatics Analysis Tool

Sequence processing utilities for NGS workflows including FASTA parsing, format conversion, and preprocessing support for downstream QC analysis.

---

## Features

- FASTA file parsing
- Nucleotide composition analysis (A, T, G, C, N)
- GC and AT content calculation
- DNA complement and reverse complement
- Codon-based protein translation (frames 1–3)
- Command-line interface (CLI)
- Installable Python package

---

## Installation

Clone the repository and install in editable mode:

```bash
git clone https://github.com/yourusername/genomic-toolkit.git
cd genomic-toolkit
pip install -e . 
```
## Usage

### GC Content
```bash
genomic-toolkit --file data/sequence.fasta --gc
```

### AT Content
```bash
genomic-toolkit --file data/sequence.fasta --at
```

### Nucleotide Composition
```bash
genomic-toolkit --file data/sequence.fasta --composition
```

### Protein Translation (Frame 1-3)
```bash
genomic-toolkit --file data/sequence.fasta --translate 1
```

### Save Output to File
```bash
genomic-toolkit --file data/sequence.fasta --gc --out results.txt
```

## Project Structure

```text
genomic-toolkit/
├── src/
│   └── genomic_toolkit/
│       ├── cli.py
│       ├── fasta_analysis.py
│       ├── sequence_translation.py
│       └── __init__.py
│
├── data/
│   └── sequence.fasta
│
├── tests/
│   └── (future test files)
│
├── pyproject.toml
├── README.md
└── .gitignore
```
## Example Output
GC content: 43.27%

Translation (frame 1):
MKTLLV...

## Tech Stack
- Python 3.8+
- argparse (CLI interface)
- setuptools (packaging)
- Standard library only (no external dependencies)

## Purpose
This project demonstrates:

- Modular software design in Python
- CLI tool development for bioinformatics workflows
- FASTA file processing and sequence analysis
- Reproducible pipeline-style computation
- Packaging and installable Python tooling

## Future Improvements
- JSON output formatting for downstream pipelines
- Multi-FASTA file support
- FASTA format validation and error handling
- Logging system for analysis tracking

## Author

### Shiloh Cadere
### Bioinformatics Analyst | Clinical NGS Pipelines | Python / R / SQL
