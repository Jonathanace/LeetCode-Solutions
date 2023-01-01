class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split(' ')):
            return False
        letters = {}
        strings = {}
        for letter, string in zip(pattern, s.split(' ')):
            if string in strings and strings[string] != letter:
                return False
            elif letter in letters and letters[letter] != string:
                return False
            else:
                strings[string] = letter
                letters[letter] = string
        return True