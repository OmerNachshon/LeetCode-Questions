"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squares = [set() for i in range(9)]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j].isnumeric():
                    square = (i//3)*3 + j//3
                    if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[square]:
                        return False
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squares[square].add(board[i][j])
        return True
