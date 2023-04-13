class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_list = list(s)
        
        i = 0
        while i < len(t) and s_list:
            if t[i] == s_list[0]:
                s_list.pop(0)
            i += 1
            
        return not (len(s_list) > 0)