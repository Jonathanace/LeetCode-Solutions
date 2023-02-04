class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        c = collections.Counter(s1)
        for end in range(m, n+1):
            if collections.Counter(s2[end-m:end]) == c:
                return True
            
        return False