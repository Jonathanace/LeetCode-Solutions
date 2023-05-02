class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        for num in nums:
            if num == 0:
                return 0
            else:
                prod *= num
        
        return 1 if prod > 0 else -1