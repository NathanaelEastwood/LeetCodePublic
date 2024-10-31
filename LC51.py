import copy
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.current_board = [["."] * n for i in range(n)]
        y_pos = [0] * n
        result = []

        def check_current_is_valid(row_num: int, y_position: int) -> bool:
            for row in range(row_num):
                if y_pos[row] == y_position:
                    return False

            # iterate through the rows above the current row, moving one square further to either side as you go
            diagonal_offset = 1
            for row in range(row_num - 1, -1, -1):
                if y_position - diagonal_offset >= 0 and y_position - diagonal_offset == y_pos[row]:
                    return False
                if y_position + diagonal_offset < n and y_position + diagonal_offset == y_pos[row]:
                    return False
                diagonal_offset += 1

            return True

        def backtrack(row_num) -> None:
            if row_num == n:
                result.append(copy.deepcopy(self.current_board))
                return

            while y_pos[row_num] < n:
                self.current_board[row_num][y_pos[row_num]] = "Q"
                current_valid = check_current_is_valid(row_num, y_pos[row_num])
                if current_valid:
                    backtrack(row_num + 1)
                self.current_board[row_num][y_pos[row_num]] = "."
                y_pos[row_num] += 1
            y_pos[row_num] = 0
            return
        backtrack(0)

        # format the 3d output array to the desired result
        for candidate_answer in result:
            for i, row in enumerate(candidate_answer):
                candidate_answer[i] = "".join(row)

        return result
