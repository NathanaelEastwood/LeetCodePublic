from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.result = False
        char_list = list(word)
        x_length = len(board)
        y_length = len(board[0])

        def backtrack(remaining_chars: List[str], starting_location: List[int], previous_locations: List[List[int]]):
            if len(remaining_chars) == 0:
                self.result = True
                return
            for i in range(4):
                if i == 0:
                    new_square = [starting_location[0] + 1, starting_location[1] + 0]
                elif i == 1:
                    new_square = [starting_location[0] - 1, starting_location[1] + 0]
                elif i == 2:
                    new_square = [starting_location[0], starting_location[1] + 1]
                else:
                    new_square = [starting_location[0], starting_location[1] - 1]

                if previous_locations.count(new_square) < 1 and 0 <= new_square[0] < x_length and 0 <= new_square[1] < y_length and board[new_square[0]][new_square[1]] == remaining_chars[0]:
                    new_previous_locations = previous_locations[::]
                    new_previous_locations.append(new_square)
                    backtrack(remaining_chars[1:], new_square, new_previous_locations)

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == char_list[0] and not self.result:
                    backtrack(char_list[1:], [x, y], [[x,y]])

        return self.result