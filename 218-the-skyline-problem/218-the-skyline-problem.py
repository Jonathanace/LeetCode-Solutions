# source: https://leetcode.com/problems/the-skyline-problem/discuss/61210/14-line-python-code-straightforward-and-easy-to-understand/112859
from heapq import *

class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # `position` stores all coordinates where the largest height may change
        # `alive` stores all buildings whose ranges cover the current coordinate
        position = sorted(set([building[0] for building in buildings] + [building[1] for building in buildings]))
        ptr, prevH = 0, 0
        alive, ret = [], []
        
        for curPos in position:
            # pop buildings that end at or before `curPos` out of the priority queue
            # they are no longer "alive"
            while alive and alive[0][1] <= curPos:
                heappop(alive)
            
            # push [negative_height, end_point] of all buildings that start before `curPos` onto the priority queue
            # they are candidates for the current highest building
            while ptr < len(buildings) and buildings[ptr][0] <= curPos:
                heappush(alive, [-buildings[ptr][2], buildings[ptr][1]])
                ptr += 1
            
            # now alive[0] must be the largest height at the current position
            if alive:
                curH = -alive[0][0]
                if curH != prevH:
                    ret.append([curPos, curH])
                    prevH = curH
            else:  # no building -> horizon
                ret.append([curPos, 0])
                
        return ret