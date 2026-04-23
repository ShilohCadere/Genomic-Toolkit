# Genomic Toolkit — CLI Bioinformatics Analysis Tool

A modular Python command-line tool for basic genomic sequence analysis, built to simulate real-world bioinformatics preprocessing workflows including FASTA parsing, nucleotide composition analysis, and sequence translation.

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
genomic-toolkit/
│
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
├── pyproject.toml
└── README.md