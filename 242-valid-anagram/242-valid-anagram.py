class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = {}
        for i in s:
            s_d[i] = s_d.get(i, 0) + 1
        
        t_d = {}
        for i in t:
            t_d[i] = t_d.get(i, 0) + 1
            
        return s_d == t_d