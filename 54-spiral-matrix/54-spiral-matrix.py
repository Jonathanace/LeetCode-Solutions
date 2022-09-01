class Solution:
    def spiralOrder(self, grid: List[List[int]]) -> List[int]:
        height = len(grid) - 1
        width = len(grid[0]) - 1
        x = y = 0
        res = []
        while True:
            res.append(grid[y][x])
            
            # right
            for i in range(width):
                x += 1
                res.append(grid[y][x])
            
            # down
            for i in range(height):
                y += 1
                res.append(grid[y][x])
            height -= 1
            
            if width < 0 or height < 0:
                return res
            
            # left
            for i in range(width):
                x -= 1
                res.append(grid[y][x])
            width -= 1
            
            if width < 0 or height < 0:
                return res
            
            # up
            for i in range(height):
                y -= 1
                res.append(grid[y][x])
            x += 1
            height -= 1
            width -= 1
            
            if width < 0 or height < 0:
                return res