class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start = 0
        res = []
        while start < len(s):
            for end in range(start + 1, len(s) + 1):
                if set(s[start:end]).isdisjoint(set(s[end:])):
                    res.append(end - start)
                    start = end
        return res