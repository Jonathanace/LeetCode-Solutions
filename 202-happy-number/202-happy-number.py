class Solution:
    def isHappy(self, n: int) -> bool:
        mem = {}
        def check(n):
            if n == 1:
                return True
            elif n in mem:
                return False
            else:
                mem[n] = 1
                c = 0
                for i in str(n):
                    c += int(i) ** 2
                return check(c)
            
        return check(n)