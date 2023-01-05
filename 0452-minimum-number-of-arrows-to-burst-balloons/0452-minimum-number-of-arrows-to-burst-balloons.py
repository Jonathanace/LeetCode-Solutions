class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:

        points.sort(key = lambda x: x[1])
        res = 1
        prev_end = points[0][1]

        for start, end in points:
            if prev_end < start:
                prev_end = end
                res += 1
    
        return res