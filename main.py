from session_5_summary import generate_summary
from session_4_translation import translate_sequence

# The mutation scanner logic lives here
original = "AUGUUUUUCGCCUAG"
mutated = "AUGUUCGCCUUUUAG"  # Example mutation

if len(original) == len(mutated):
    mutation_count = 0
    for i in range(len(original)):
        if original[i] != mutated[i]:
            print(f"Mutation found at index: {i+1}: {original[i]} -> {mutated[i]}")
            mutation_count += 1
    orig_protein = translate_sequence(original)
    mut_protein  = translate_sequence(mutated)
    if orig_protein == mut_protein:
        mutation_type = "Silent Mutation"
    elif "Stop" in mut_protein and "Stop" not in orig_protein:
        mutation_type = "Nonsense Mutation"
    else:
        mutation_type = "Missense Mutation"
    
    generate_summary(len(original), mutation_count, mutation_type, orig_protein, mut_protein)
            
else:
    print(f"Error: Sequences must be of same length")    

print("Original Protein:", translate_sequence(original))
print("Mutated Protein: ", translate_sequence(mutated))