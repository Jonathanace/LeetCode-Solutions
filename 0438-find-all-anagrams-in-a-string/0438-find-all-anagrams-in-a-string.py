class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = sorted(p)
        res = []
        l = len(s)
        for start in range(l-len(p)+1):
            window = sorted(s[start:start+len(p)])
            if window == p:
                res.append(start)
                
        return res