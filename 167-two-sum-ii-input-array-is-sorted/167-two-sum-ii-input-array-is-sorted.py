class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevs = {} # number: index
        s = set()
        i = 0
        while True:
            while i < len(numbers) - 1 and numbers[i+1] == numbers[i]:
                prevs[numbers[i]] = i
                i += 1

            sub = target - numbers[i]
            if sub in prevs:
                return [prevs[sub]+1, i+1]
            else:
                prevs[numbers[i]] = i
                i += 1