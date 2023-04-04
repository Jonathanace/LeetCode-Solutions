class Solution:
    def partitionString(self, s: str) -> int:
        prevs = set()
        res = 1
        for i in s:
            if i in prevs:
                res += 1
                prevs = set()
            prevs.add(i)
                
        return res