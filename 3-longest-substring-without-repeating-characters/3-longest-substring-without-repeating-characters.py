class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end, max_len = 0, 0, 0
        string = []
        while end < len(s):
            while s[end] in string:
                string.pop(0)
                start += 1
            string.append(s[end])
            max_len = max(max_len, len(string))
            end += 1
        return max_len