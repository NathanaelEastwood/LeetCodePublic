from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # search that each row does not include duplicates
        for x in range(9):
            check_map = {}
            for y in range(9):
                if check_map.get(board[x][y]) == 1:
                    return False
                elif board[x][y] != '.':
                    check_map[board[x][y]] = 1

        # search that each column does not include duplicates

        for y in range(9):
            check_map = {}
            for x in range(9):
                if check_map.get(board[x][y]) == 1:
                    return False
                elif board[x][y] != '.':
                    check_map[board[x][y]] = 1

        # search that each square does not include duplicates

        for square_x in range(3):
            for square_y in range(3):
                check_map = {}
                for i in range(3):
                    for j in range(3):
                        if check_map.get(board[square_x*3 + i][square_y*3 + j]) == 1:
                            return False
                        elif board[square_x*3 + i][square_y*3 + j] != '.':
                            check_map[board[square_x*3 + i][square_y*3 + j]] = 1




        return True
