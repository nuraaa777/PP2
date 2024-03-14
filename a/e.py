import re

def match_string(text):
    pattern = r'a.*b$'
    if re.search(pattern, text):
        return True
    else:
        return False

# Test the function
test_strings = ["ab", "acb", "abbb", "aabb", "a1234b", "a b", "a", "abbbbbc"]
for test_string in test_strings:
    print(f"{test_string}: {match_string(test_string)}")

