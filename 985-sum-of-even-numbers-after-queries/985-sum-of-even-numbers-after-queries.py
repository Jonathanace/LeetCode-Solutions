class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum([i for i in nums if i % 2 == 0])
        res = []
        for val, index in queries:
            if nums[index] % 2 == 0:
                even_sum -= nums[index]
            nums[index] += val
            if nums[index] % 2 == 0:
                even_sum += nums[index]
            res.append(even_sum)
        return res