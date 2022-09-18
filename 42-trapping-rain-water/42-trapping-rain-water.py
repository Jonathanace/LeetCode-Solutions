# source: https://leetcode.com/problems/trapping-rain-water/discuss/17364/7-lines-C-C++/447098
class Solution:
    def trap(self, h: List[int]) -> int:
        l = 0
        r = len(h) - 1
        ceil = 0 
        res = 0
        
        while l < r: 
            if h[l] < h[r]:
                floor = h[l]
                l += 1
            else:
                floor = h[r]
                r -= 1
                
            ceil = max(ceil, floor)
            res += (ceil - floor)
        
        return res