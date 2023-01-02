class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        if not word[0].isupper(): # if the first letter is lowercase
            for letter in word[1:]:
                if letter.isupper():
                    return False
            return True
        elif word[1].isupper(): # all letters must be uppercase
            return True if word[1:].isupper() else False
        else: # all letters except the first must be lowercase
            for letter in word[1:]:
                if letter.isupper():
                    return False
            return True