class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == "." : 
                    continue
                if board[i][j] in seen :
                    return False
                seen.add(board[i][j])
        for col in range(9):
            seen = set()
            for j in range(9):
                if board[j][col] == ".":
                    continue
                if board[j][col] in seen:
                    return False
                seen.add(board[j][col])
        for sub_col in range(9):
            seen = set()
            for sub_row in range(3):
                for j in range(3):
                    row = (sub_col // 3) * 3 + sub_row
                    col = (sub_col % 3) *3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True

                








"""
[["1","2","."]
 ["4",".","."]
 [".","9","8"]
 ]
 
"""