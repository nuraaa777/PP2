import re

def find_sequences(text):
    pattern = r'[A-Z][a-z]+'
    sequences = re.findall(pattern, text)
    return sequences

# Test the function
text = "This is a Sample Text With Sequences Like This One"
sequences = find_sequences(text)
print("Sequences found:", sequences)


