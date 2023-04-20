class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares, rows, columns = defaultdict(set), defaultdict(set), defaultdict(set)
        for row in range(9):
            for column in range(9):
                num = board[row][column]
                if num == '.':
                    continue
                else:
                    num = int(num)
                
                if num in rows[row]:
                    # print(num, row)
                    return False
                else:
                    rows[row].add(num)
                    
                if num in columns[column]:
                    # print(num, column)
                    return False
                else:
                    columns[column].add(num)
                    
                square = (row // 3, column // 3)
                if num in squares[square]:
                    # print(num, square)
                    return False
                else:
                    squares[square].add(num)
        return True
#0, 1, 2
#3, 4, 5
#6, 7 8