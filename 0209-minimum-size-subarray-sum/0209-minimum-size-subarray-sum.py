class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: 
            return 0
        
        res = len(nums)
        start = 0
        
        for end in range(0, len(nums)):
            target -= nums[end]
            while target <= 0:
                res = min(res, end - start + 1)
                target += nums[start]
                start += 1
        
        return res