class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        res = [n for _ in range(n)]
        
        res[0] = 0
        # print(res)
        for i in range(n):
            for j in range(i, min(n, i + nums[i] + 1)):
                res[j] = min(res[j], res[i] + 1)
            # print(res)
                
        return res[-1]