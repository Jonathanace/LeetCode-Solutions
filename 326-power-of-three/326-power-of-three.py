class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x = 0
        while (3 ** x) < n:
            x += 1
        return True if (3 ** x) == n and n >= 0 else False