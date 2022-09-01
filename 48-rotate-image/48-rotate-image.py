class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix.reverse()
        for row in range(n):
            for column in range(row): 
                matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
        return matrix