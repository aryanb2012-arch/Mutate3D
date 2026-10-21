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
- **Gene Sequence Scanner**: Sweeps across complete multi-codon mRNA strands in steps of 3 bases using index math (`range(0, len(seq), 3)`), detecting and logging every mutation's exact sequence position and type.
- **RNA Translation Engine**: Converts codons into amino acids and detects start(AUG) and stop codons(UAG,UAA,UGA)
  
## 💻 Tech Stack
- **Language**: Python 3
- **Core Concepts**: Dictionaries, String Slicing, Step-based Loops, Conditional Logic (`if/elif/else`), Modular Functions,Scope & Modular Architecture (Passing parameters into functions and logging output via `return` values)

## 🚀 Quick Usage
```python
# Classify point mutations between original and mutated codons
classify_mutation("UUU", "UUC")  # Output: Silent
classify_mutation("AUG", "GCU")  # Output: Missense
classify_mutation("GCU", "UAG")  # Output: Nonsense
# Initialize RNA strands
original_gene = "AUGUUUGCU"
mutated_gene  = "AUGUUCUAG"

# Scan strands and log detected mutations
results = scan_gene_mutations(original_gene, mutated_gene)
print(results)

# Output:
# ['Position 3: UUU -> UUC (Silent)', 'Position 6: GCU -> UAG (Nonsense)']

#Example of how the RNA translation engine works:
#Input: "GCUAUGUUUUUCGCCUAG"
#Output: "M-F-F-A" (Disregards the codons until the start codon "AUG")
