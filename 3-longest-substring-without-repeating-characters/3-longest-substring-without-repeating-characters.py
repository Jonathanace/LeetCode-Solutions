class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        max_len = 0
        string = []
        repeats = False
        prevs = set()
        while end < len(s):
            while s[end] in string:
                string.pop(0)
                start += 1
            string.append(s[end])
            print(string)
            max_len = max(max_len, len(string))
            end += 1
        return max_len