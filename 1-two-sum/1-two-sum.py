class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            num = target - nums[i]
            if num in d:
                return [i, d[num]]
            d[nums[i]] = i