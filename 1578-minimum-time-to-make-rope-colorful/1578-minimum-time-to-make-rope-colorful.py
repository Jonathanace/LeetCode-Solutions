class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        i = 0
        while i < len(colors):
            # find span of same colored baloons
            j = i + 1
            while j < len(colors) and colors[j] == colors[i]:
                j += 1
                
            # delete all baloons except the one that takes the most time to remove
            time += sum(sorted(neededTime[i:j])[:-1])
            
            # update i
            i = j-1
            i += 1
        return time