class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = 1
        while x < n:
            x *=4
        return True if x == n else False