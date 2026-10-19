# Mutate3D 🧬

A python-based bioinformatics tool designed to translate RNA sequences and analyze point mutations.I am creating a 3D Mutation Visualizer to learn more about Biology, Chemistry and Coding while trying to create a project that is not only fun to make on the way but also can make learning more interactive rather than just textbook learning

## 📌 Project Overview
Mutate3D bridges molecular biology and computer science by simulating how mRNA sequences translate into protein chains and evaluating the impact of genetic mutations.

## ✨ Features
- **RNA Sequence Translator**: Parses mRNA sequences in 3-letter codons to build translated protein chains.
- **Mutation Classifier Engine**: Compares codon pairs to identify and classify single-nucleotide variants into three biological categories:
  - **Silent**: Codon changes, but the translated amino acid remains identical.
  - **Missense**: Codon changes, resulting in a different amino acid.
  - **Nonsense**: Codon changes into a premature **STOP** signal.

## 💻 Tech Stack
- **Language**: Python 3
- **Core Concepts**: Dictionaries, String Slicing, Step-based Loops, Conditional Logic (`if/elif/else`), Modular Functions

## 🚀 Quick Usage
```python
# Classify point mutations between original and mutated codons
classify_mutation("UUU", "UUC")  # Output: Silent
classify_mutation("AUG", "GCU")  # Output: Missense
classify_mutation("GCU", "UAG")  # Output: Nonsense
