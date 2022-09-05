class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        d = {}
        for i in words: # search for outside values
            if i[::-1] in d and d[i[::-1]] > 0:
                d[i[::-1]] -= 1
                res += 4
            else:
                d[i] = d.get(i, 0) + 1
                
        for i in d.keys(): # search for middle value
            if i[0] == i[1] and d[i] > 0:
                res += 2
                break
        return res