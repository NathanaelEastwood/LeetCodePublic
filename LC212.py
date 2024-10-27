from copy import copy
from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.trie = Trie()
        self.bottom_edge = len(board) - 1
        self.right_edge = len(board[0]) - 1
        self.board = board
        result = []

        for word in words:
            self.trie.add_word(word)

        for n in range(len(self.board)):
            for m in range(len(self.board[0])):
                self.return_value = []
                current_set = set()
                current_set.add((n, m))
                search_result = self.search_square((n,m), board[n][m], current_set)
                if len(search_result) > 0:
                    for word in search_result:
                        result.append(word)

        return result

    def search_square(self, current_location, word: str, previous_locations) -> (bool, List[str]):
        result_on_square = self.trie.search_prefix_or_word(word)
        if result_on_square[1]:
            self.return_value.append(word)
            self.trie.remove_word(word)
        if result_on_square[0]:
            for i in range(4):
                word_temp = word
                temp_previous_locations = copy(previous_locations)
                if i == 0:
                    surrounding_square = (current_location[0] + 1, current_location[1])
                elif i == 1:
                    surrounding_square = (current_location[0] - 1, current_location[1])
                elif i == 2:
                    surrounding_square = (current_location[0], current_location[1] + 1)
                else:
                    surrounding_square = (current_location[0], current_location[1] - 1)

                if 0 <= surrounding_square[0] <= self.bottom_edge and 0 <= surrounding_square[1] <= self.right_edge:
                    word_temp += self.board[surrounding_square[0]][surrounding_square[1]]
                    old_len = len(temp_previous_locations)
                    temp_previous_locations.add(surrounding_square)
                    new_len = len(temp_previous_locations)
                    if old_len != new_len:
                        self.search_square(surrounding_square, word_temp, temp_previous_locations)

        return self.return_value



class Trie:
    def __init__(self):
        self.children = {}
        self.word_end = False
        self.paths_accessing = 1

    def add_word(self, word: str):
        curr = self
        for c in word:
            c_index = ord(c) - ord('a')
            if not curr.children.get(c_index):
                curr.children[c_index] = Trie()
            curr.paths_accessing += 1
            curr = curr.children[c_index]
        curr.word_end = True

    def remove_word(self, word) -> None:
        curr = self
        for c in word:
            c_index = ord(c) - ord('a')
            if curr.children.get(c_index) is None:
                break
            curr.paths_accessing -= 1
            if curr.paths_accessing == 1:
                curr.children[c_index] = None
                break
            curr = curr.children[c_index]
        curr.word_end = False


    def search_prefix_or_word(self, input_word: str) -> (bool, bool):
        is_valid_prefix = True
        curr = self
        for c in input_word:
            c_index = ord(c) - ord('a')
            if not curr.children.get(c_index):
                return False, False
            curr = curr.children[c_index]

        is_valid_word = curr.word_end
        return is_valid_prefix, is_valid_word
