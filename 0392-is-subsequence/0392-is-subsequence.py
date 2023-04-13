class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in t:
            if s.startswith(i):
                s = s[1:]
        return not bool(len(s))