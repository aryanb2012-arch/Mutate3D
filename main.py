from session_4_translation import translate_sequence

# The mutation scanner logic lives here
original = "AUGUUUUUCGCCUAG"
mutated = "AUGUUCGCCUUUUAG"  # Example mutation

if len(original) == len(mutated):
    for i in range(len(original)):
        if original[i] != mutated[i]:
            print(f"Mutation found at index: {i+1}: {original[i]} -> {mutated[i]}")
else:
    print(f"Error: Sequences must be of same length")    

print("Original Protein:", translate_sequence(original))
print("Mutated Protein: ", translate_sequence(mutated))