class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares, rows, columns = defaultdict(set), defaultdict(set), defaultdict(set)
        for row in range(9):
            for column in range(9):
                # check for valid number
                try:
                    num = int(board[row][column])
                except:
                    continue
                
                # check row
                if num in rows[row]:
                    return False
                else:
                    rows[row].add(num)
                    
                # check column
                if num in columns[column]:
                    return False
                else:
                    columns[column].add(num)
                    
                # check square
                square = (row // 3, column // 3)
                if num in squares[square]:
                    return False
                else:
                    squares[square].add(num)
        
        return True 