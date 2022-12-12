class Solution:
    def climbStairs(self, n: int) -> int:
        d = {
            1: 1,
            2: 2,
            3: 3,
            4: 5
        }
    
        def tab(n):
            if n not in d:
                d[n] = tab(n-1) + tab(n-2)
            return d[n]
        
        return tab(n)