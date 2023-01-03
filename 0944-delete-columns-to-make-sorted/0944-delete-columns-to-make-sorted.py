class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for i in range(len(strs[0])):
            l = [j[i] for j in strs]
            if l != sorted(l):
                res += 1
        return res