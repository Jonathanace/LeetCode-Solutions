class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in nums:
            if num not in s:
                continue
            count = 1
            s.remove(num)
            low = num - 1
            high = num + 1
            while low in s:
                count += 1
                s.remove(low)
                low -= 1
            while high in s:
                count += 1
                s.remove(high)
                high += 1
            res = max(res, count)
        
        return res