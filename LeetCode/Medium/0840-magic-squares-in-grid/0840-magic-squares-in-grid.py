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
        if grid[row+1][col+1] != 5:
            return False
        
        offsets = [(offset_row, offset_col) for offset_row in range(3) for offset_col in range(3)]
        vals = [grid[row+offset_row][col+offset_col] for offset_row, offset_col in offsets]
        if sorted(vals) != [1,2,3,4,5,6,7,8,9]:
            return False

        v_1 = vals[0] + vals[3] + vals[6]
        v_2 = vals[1] + vals[4] + vals[7]
        v_3 = vals[2] + vals[5] + vals[8]
        h_1 = vals[0] + vals[1] + vals[2]
        h_2 = vals[3] + vals[4] + vals[5]
        h_3 = vals[6] + vals[7] + vals[8]
        d_1 = vals[0] + vals[4] + vals[8]
        d_2 = vals[6] + vals[4] + vals[2]

        return v_1 == v_2 == v_3 == h_1 == h_2 == h_3 == d_1 == d_2