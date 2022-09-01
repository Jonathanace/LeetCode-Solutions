class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        height = len(grid)
        width = len(grid[0])
        
        def test(x):
            for y in range(height):
                new_x = x + grid[y][x]
                if new_x < 0 or new_x >= width or grid[y][new_x] != grid[y][x]:
                    return -1
                x = new_x
            return x
        
        return [test(i) for i in range(width)]