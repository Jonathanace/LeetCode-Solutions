class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        old_m = copy.deepcopy(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = old_m[-(j+1)][i]