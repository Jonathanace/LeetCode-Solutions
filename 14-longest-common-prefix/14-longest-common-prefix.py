class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        min_l = min([len(i) for i in strs])
        for i in range(min_l):
            if len(set([string[i] for string in strs])) == 1:
                   res += (strs[0][i])
            else:
                break
        return res