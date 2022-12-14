class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom up dp
        l = len(nums)
        if l == 1:
            return nums[0]
        
        dp = {0: nums[0], 1: nums[1]}
        maximum = max(nums[:2])
        
        def recur(i): 
            if i not in dp:
                dp[i] = max([recur(i) for i in range(i-1)]) + nums[i]
            return dp[i]
        
        for house in range(2, len(nums)):
            maximum = max(maximum, recur(house))
            
        return maximum