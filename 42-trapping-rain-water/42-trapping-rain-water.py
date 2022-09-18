class Solution:
    def trap(self, h: List[int]) -> int:
        l = 0
        r = len(h) - 1
        floor = 0 
        res = 0
        
        while l < r: 
            if h[l] < h[r]:
                lower = h[l]
                l += 1
            else:
                lower = h[r]
                r -= 1
                
            floor = max(floor, lower)
            res += (floor - lower)
        
        return res