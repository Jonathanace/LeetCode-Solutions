class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = defaultdict(list)
        columns = defaultdict(list)
        rows = defaultdict(list)
        
        for row in range(9):
            # print()
            for column in range(9):
                num = board[row][column]
                # print(num,end='')
                if num == '.':
                    continue
                else:
                    num = int(num)
                # print(row, column, num)
                if num in squares[(row//3, column//3)] or num in rows[row] or num in columns[column]:
                    return False
                squares[(row//3, column//3)].append(num)
                rows[row].append(num)
                columns[column].append(num)
                
        return True