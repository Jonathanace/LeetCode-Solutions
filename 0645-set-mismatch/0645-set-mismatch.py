class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = [i for i in range(1, len(nums)+1)]
        s = set(nums)
        for i in range(1, len(nums)+1):
            if i not in nums:
                skipped = i
                break
                
        prevs = set()
        for i in nums:
            if i in prevs:
                repeated = i
                break
            prevs.add(i)
            
        return [repeated, skipped]