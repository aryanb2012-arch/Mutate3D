from session_4_translation import translate_sequence

# The mutation scanner logic lives here
original = "AUGUUUUUCGCCUAG"
mutated = "AUGUUCGCCUUUUAG"  # Example mutation

if len(original) == len(mutated):
    for i in range(len(original)):
        if original[i] != mutated[i]:
            print(f"Mutation found at index: {i+1}: {original[i]} -> {mutated[i]}")
    orig_protein = translate_sequence(original)
    mut_protein  = translate_sequence(mutated)
    if orig_protein == mut_protein:
        print(f"Silent Mutation: Does not change the final amino acid")
    elif "Stop" in mut_protein and "Stop" not in orig_protein:
        print(f"Nonense Mutation: Prematurely stops the sequence")
    else:
        print(f"Missense Mutation: Completely changes the amino acid ")
            
else:
    print(f"Error: Sequences must be of same length")    

print("Original Protein:", translate_sequence(original))
print("Mutated Protein: ", translate_sequence(mutated))