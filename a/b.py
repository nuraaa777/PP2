import re

def match_string(text):
    pattern = r'a(bb|bbb)'
    if re.search(pattern, text):
        return True
    else:
        return False

# Test the function
test_strings = ["ab", "abb", "abbb", "abbbb", "aabb", "aabbb", "aaabbb"]
for test_string in test_strings:
    print(f"{test_string}: {match_string(test_string)}")

