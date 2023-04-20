class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        pre = 1
        for i in range(0, n, 1):
            res[i] *= pre
            pre *= nums[i]
        
        post = 1
        for i in range(n-1, -1, -1):
            res[i] *= post
            post *= nums[i]
            
        return res