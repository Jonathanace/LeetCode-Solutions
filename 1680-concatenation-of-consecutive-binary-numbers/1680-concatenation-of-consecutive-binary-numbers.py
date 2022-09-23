class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10 ** 9 + 7
        binary = ''.join([bin(i)[2:] for i in range(1, n+1)])
        return int(binary, 2) % mod