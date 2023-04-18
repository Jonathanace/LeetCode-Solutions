class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        res = ''
        i = 0
        
        while i < min(n, m):
            res += word1[i]
            res += word2[i]
            i += 1
        if n > m:
            res += word1[m:n]
        elif m > n:
            res += word2[n:m]
        
        return res