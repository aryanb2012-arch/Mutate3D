original = ("AUGUUU")
mutated = ("AUGUUC")

if len(original) == len(mutated):
    for i in range(len(original)):
        if original[i] != mutated[i]:
            print(f"Mutation found at index: {i+1}: {original[i]} -> {mutated[i]}")
else:
    print(f"Error: Sequences must be of same length")
    
