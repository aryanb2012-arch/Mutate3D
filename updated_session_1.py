def count_bases(dna_sequence):
    count = len(dna_sequence)
    return count

result = count_bases("ATGCGAT")
print(result)

def check_start_codon(codon):
    if codon == "AUG":
        return ("Start codon count")
    else:
        return("No start codon")

result = check_start_codon("AUG")
print(result)

result2 = check_start_codon("UAC")
print(result2)

def translate_codon(codon):
    code = {"AUG":"M","UUU":"F","UAG":"STOP"}
    return code.get(codon, "Unknown")
answer = translate_codon("GGC")

print(answer)

def translate_sequence(rna_sequence):
    protein = []
    for i in range(0, len(rna_sequence), 3):
        amino_acid = translate_codon(rna_sequence[i:i+3])
        protein.append(amino_acid)
    return protein

print(translate_sequence("AUGUUUUAG"))