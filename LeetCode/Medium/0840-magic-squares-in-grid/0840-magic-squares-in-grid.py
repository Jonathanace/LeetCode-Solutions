class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        rows, cols = len(grid), len(grid[0])
        for row in range(rows-2):
            for col in range(cols-2):
                if self.isMagicSquare(grid, row, col):
                    count += 1
        return count

    def isMagicSquare(self, grid: List[List[int]], row: int, col: int) -> bool:
        offsets = [(offset_row, offset_col) for offset_row in range(3) for offset_col in range(3)]
        vals = [grid[row+offset_row][col+offset_col] for offset_row, offset_col in offsets]
        if set(vals) != set(range(1,10)):
            return False
        v_1 = vals[0] + vals[3] + vals[6]
        v_2 = vals[1] + vals[4] + vals[7]
        if v_1 != v_2:
            return False
        v_3 = vals[2] + vals[5] + vals[8]
        if v_3 != v_2:
            return False
        h_1 = vals[0] + vals[1] + vals[2]
        if h_1 != v_3: 
            return False
        h_2 = vals[3] + vals[4] + vals[5]
        if h_2 != h_1:
            return False
        h_3 = vals[6] + vals[7] + vals[8]
        if h_3 != h_2:
            return False
        d_1 = vals[0] + vals[4] + vals[8]
        if d_1 != h_3:
            return False
        d_2 = vals[6] + vals[4] + vals[2]
        if d_2 != d_1:
            return False

        return True