
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
