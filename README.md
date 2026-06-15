# Genomic Toolkit

## Recruiter Summary

A Python-based bioinformatics toolkit for FASTA parsing, sequence analysis, protein translation, and command-line processing of nucleotide sequence data.

This project demonstrates modular Python development, command-line tool design, biological sequence manipulation, and packaging of reusable bioinformatics utilities into an installable software package.

## What This Project Demonstrates

* Developing modular bioinformatics software in Python
* Building command-line interfaces for biological data analysis
* Parsing and processing FASTA-formatted sequence files
* Calculating nucleotide composition metrics
* Performing codon-based protein translation
* Organizing reusable functionality into a package structure
* Creating installable Python tooling for sequence analysis tasks

## Features

* FASTA file parsing
* Nucleotide composition analysis (A, T, G, C, N)
* GC content calculation
* AT content calculation
* DNA complement generation
* Reverse complement generation
* Codon-based protein translation (Frames 1–3)
* Command-line interface (CLI)
* Installable Python package structure

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
│
├── requirements.txt
├── README.md
└── .gitignore
```

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

### Protein Translation

```bash
genomic-toolkit --file data/sequence.fasta --translate 1
```

### Save Output to File

```bash
genomic-toolkit --file data/sequence.fasta --gc --out results.txt
```

## Example Output

```text
GC Content: 43.27%

A: 112
T: 97
G: 84
C: 82
N: 0

Translation (Frame 1):
MKTLLV...
```

## Technology Stack

**Python** • **argparse** • **FASTA Processing** • **Command-Line Interfaces** • **Bioinformatics Utilities**

## Design Goals

This project focuses on:

* Reusable sequence analysis utilities
* Modular software organization
* Command-line bioinformatics workflows
* Readable and maintainable Python code
* Lightweight tooling with minimal dependencies

## Future Enhancements

* Multi-FASTA support
* FASTA validation and error handling
* Expanded sequence QC metrics
* Unit test coverage
* Enhanced logging and execution reporting

## Author

**Shiloh Cadere**
Bioinformatics Analyst specializing in genomics QC, data validation, workflow development, and laboratory data systems.
