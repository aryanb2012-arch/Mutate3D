from session_4_translation import translate_sequence

# The mutation scanner logic lives here
original_gene = "AUGUUUUUCGCCUAG"
mutated_gene  = "AUGUUCGCCUAG"  # Example mutation

print("Original Protein:", translate_sequence(original_gene))
print("Mutated Protein: ", translate_sequence(mutated_gene))