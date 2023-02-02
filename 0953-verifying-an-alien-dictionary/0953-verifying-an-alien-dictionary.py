class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        prev_word = words[0]
        for word in words[1:]:
            l = min(len(word), len(prev_word))
            i = 0
            while i < l:
                # print(word[i])
                if order.index(word[i]) > order.index(prev_word[i]):
                    break
                elif order.index(word[i]) == order.index(prev_word[i]):
                    i += 1
                elif order.index(word[i]) < order.index(prev_word[i]):
                    return False
            if i == l and len(prev_word) > len(word):
                return False
            prev_word = word
        return True