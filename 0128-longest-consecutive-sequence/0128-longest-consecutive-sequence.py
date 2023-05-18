class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in s:
            if num-1 not in s:
                count = 1
                cur = num
                while cur in s:
                    res = max(res, count)
                    count += 1
                    cur += 1
        
        return res