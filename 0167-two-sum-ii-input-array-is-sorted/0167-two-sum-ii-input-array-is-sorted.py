class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        s = numbers[i] + numbers[j]
        while s != target:
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            s = numbers[i] + numbers[j]
        return [i + 1, j + 1]