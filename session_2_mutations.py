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
        return("Silent")
    elif mut_cod == "STOP":
        return("Nonsense")
    else:
        return("Missense")

print(classify_mutation("UUU", "UUC"))  # Should output: Silent
print(classify_mutation("AUG", "GCU"))  # Should output: Missense
print(classify_mutation("GCU", "UAG"))  # Should output: Nonsense