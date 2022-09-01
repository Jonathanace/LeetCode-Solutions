class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        depths = []
        locs = []
        self.res = 0
        height = len(grid)
        width = len(grid[0])
        
        for row in range(height): 
            for column in range(width):
                if grid[row][column] == 2:
                    depths.append(0)
                    locs.append([row, column])
                    
        def bfs(depth, row, column):
            if row < 0 or column < 0 or row > height - 1 or column > width - 1 or grid[row][column] != 1:
                return
            print(depth, '', row, column)
            self.res = max(self.res, depth)
            grid[row][column] = 2
            depths.append(depth)
            locs.append([row, column])
            
        for depth, loc in zip(depths, locs):
            row, column = loc[0], loc[1]
            if grid[row][column] == 2:
                bfs(depth+1, row-1, column)
                bfs(depth+1, row+1, column)
                bfs(depth+1, row, column-1)
                bfs(depth+1, row, column+1)
            
            
        s = set([i for sublist in grid for i in sublist])
        return -1 if 1 in s else self.res