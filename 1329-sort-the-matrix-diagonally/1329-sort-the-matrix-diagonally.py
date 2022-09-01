class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        width = len(mat[0])
        height = len(mat)
        res = mat[:]
        
        for column in range(len(mat[0])):
            buffer = []
            coords = []
            row = 0
            
            while column < width and row < height: 
                buffer.append(mat[row][column])
                coords.append([row, column])
                row += 1
                column += 1
            buffer.sort()
            
            for coord, value in zip(coords, buffer):
                x, y = coord
                res[x][y] = value    
    
        for row in range(1, len(mat)):
            buffer = []
            coords = []
            column = 0
            
            while column < width and row < height:
                buffer.append(mat[row][column])
                coords.append([row, column])
                row += 1
                column += 1
            buffer.sort()
            
            for coord, value in zip(coords, buffer):
                x, y = coord
                res[x][y] = value
            
        return res