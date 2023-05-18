class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        d = {}
        res = set()
        for i in range(n):
            prevs = {}
            for j in range(i+1, n):
                if -nums[j] in prevs:
                    n1, n2 = prevs[-nums[j]]
                    n3 = nums[j]
                    tup = tuple(sorted([n1, n2, n3]))
                    res.add(tup)
                prevs[nums[i] + nums[j]] = [nums[i], nums[j]]
                    
        return list(res)