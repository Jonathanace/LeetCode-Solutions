class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        for index, i in enumerate(reversed(num1)):
            a = (10 ** index) * int(i)
            for index, j in enumerate(reversed(num2)):
                b = (10 ** index) * int(j)
                res += a * b
        return str(res)