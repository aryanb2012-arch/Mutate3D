code = {
    "AUG": "M",  # Methionine (Start)
    "UUU": "F",  # Phenylalanine
    "UUC": "F",  # Phenylalanine
    "GCU": "A",  # Alanine
    "GCC": "A",  # Alanine
    "UAG": "STOP", # Stop
    "UAA": "STOP"  # Stop
}

def translate_codon(codon):
    return code.get(codon, "Unknown")

def classify_mutation(original_codon, mutated_codon):
    orig_cod = translate_codon(original_codon)
    mut_cod = translate_codon(mutated_codon)
    if orig_cod == mut_cod:
        return "Silent"
    elif mut_cod == "STOP":
        return "Nonsense"
    else:
        return "Missense"

def scan_gene_mutations(seq1,seq2):
    mutation_log = []
    for i in range(0,len(seq1),3):
        orig_codon = seq1[i:i+3]
        mut_codon = seq2[i:i+3]
        if orig_codon != mut_codon:
            mutation_type = classify_mutation(orig_codon, mut_codon)
            mutation_log.append(f"Position {i}: {orig_codon} -> {mut_codon} ({mutation_type}) ")
    return mutation_log

original_gene = "AUGUUUGCU"
mutated_gene  = "AUGUUCUAG"

results = scan_gene_mutations(original_gene, mutated_gene)
print(results)
        