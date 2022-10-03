class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        start = 0
        while start < len(colors):
            # find span of same colored baloons
            end = start + 1
            while end < len(colors) and colors[end] == colors[start]:
                end += 1
                
            # remove all baloons except the one that takes the most time to remove
            time += sum(sorted(neededTime[start:end])[:-1])
            
            # update start
            start = end-1
            start += 1
            
        return time