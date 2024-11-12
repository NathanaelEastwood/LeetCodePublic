from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        move_directions = {
            0: (1, 2),
            1: (2, 1),
            2: (-1, 2),
            3: (-2, 1),
            4: (-1, -2),
            5: (-2, -1),
            6: (1, -2),
            7: (2, -1)
        }
        n = len(grid)
        current_square_number = 0
        current_square_location = [0, 0]
        while current_square_number < (n * n):
            current_square_number += 1
            i = 0
            while i in range(8):
                offset = move_directions[i]
                temp_square = current_square_location[::]
                temp_square[0] += offset[0]
                temp_square[1] += offset[1]
                if 0 <= current_square_location[0] < n and 0 <= current_square_location[1] < n and grid[current_square_location[0]][current_square_location[1]] == current_square_number:
                    current_square_location = temp_square
                    break
                else:
                    i += 1
                if i == 8:
                    return False
        return True