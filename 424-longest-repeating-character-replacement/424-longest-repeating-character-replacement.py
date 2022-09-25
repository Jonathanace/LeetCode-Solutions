class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, res, counts = 0, 0, {}
        for end in range(len(s)):
            counts[s[end]] = counts.get(s[end], 0) + 1
            if end - start + 1 - max(counts[key] for key in counts.keys()) > k: 
                counts[s[start]] -= 1
                start += 1
            res = max(res, end - start + 1)
            
        return res
                