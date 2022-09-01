class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        rows = len(heights)
        columns = len(heights[0])
        pacific = set()
        atlantic = set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        def dfs(row, column, ocean): 
            if (row, column) in ocean: 
                return 
            ocean.add((row, column))
            
            for direction in directions:
                new_row, new_column = row + direction[0], column + direction[1]
                if 0 <= new_row < rows and 0 <= new_column < columns and heights[new_row][new_column] >= heights[row][column]:
                    dfs(new_row, new_column, ocean)
                    
        for row in range(rows):
            dfs(row, 0, pacific)
            dfs(row, columns-1, atlantic)
        for column in range(columns): 
            dfs(0, column, pacific)
            dfs(rows-1, column, atlantic)
            
        return list(pacific & atlantic)