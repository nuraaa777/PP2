import re

def find_sequences(text):
    pattern = r'\b[a-z]+_[a-z]+\b'
    sequences = re.findall(pattern, text)
    return sequences

# Test the function
text = "hello_world is_a_sequence of_lowercase_letters"
sequences = find_sequences(text)
print("Sequences found:", sequences)



