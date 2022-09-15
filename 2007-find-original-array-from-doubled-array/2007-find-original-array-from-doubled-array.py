class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        c = collections.Counter(changed)
        if c[0] % 2:
            return []
        for x in sorted(c):
            if c[x] > c[x * 2]: 
                return []
            else: 
                if x == 0:
                    c[x*2] -= c[x] // 2
                else: 
                    c[x*2] -= c[x]
                    
        return list(c.elements())