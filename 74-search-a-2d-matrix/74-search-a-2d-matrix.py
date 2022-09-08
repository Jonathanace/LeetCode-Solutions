class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        last_eles = [i[-1] for i in matrix]
        for i in range(len(last_eles)):
            if target == last_eles[i]:
                return True
            elif target < last_eles[i]:
                row = i
                break
        if row == -1:
            return False
        
        if target in matrix[row]:
            return True
        else:
            return False