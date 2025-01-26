"""
409. Longest Palindrome

Given a string text which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.

For this question, letters are case-sensitive, for example, "Aa" is not considered a palindrome.
"""
# Change this function so it works correctly
def longest_palindrome_length(text):
    original = set()
    repeated = set()
    for letter in text:
        if letter in original:
            repeated.add(letter)
        else:
            original.add(letter)
    length = len(text) - len(set(text)) + len(repeated) + 1
    return length


if __name__ == '__main__':
    test_cases = [('abccccdd', 7),      # dccaccd / dccbccd
                  ('a', 1),             # a
                  ('school', 3)]        # oso / oco / oho / olo

    for test_text, expected in test_cases:
        result = longest_palindrome_length(test_text)
        msg = 'Correct' if expected == result else 'Wrong'
        print(f'[{msg:7s}] longest_palindrome_length("{test_text}") should be {expected}')
