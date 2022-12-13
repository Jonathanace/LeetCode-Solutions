class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for row in range(1, len(matrix)): # for each row
            matrix[row][0] += min(matrix[row-1][:2]) # first column
            for column in range(1, len(matrix[0])-1): # middle columns
                matrix[row][column] += min(matrix[row-1][column-1:column+2])
            matrix[row][-1] += min(matrix[row-1][-2:])
                
        return min(matrix[-1])