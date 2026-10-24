def read_sequence_file(filename):
    with open(filename, "r") as file:
        sequence = file.read().strip()
    return sequence

my_sequence = read_sequence_file("sequence.txt")
print(f"Successfully loaded sequence: {my_sequence}")