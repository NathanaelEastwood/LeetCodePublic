from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        key_lookup = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        result = []
        def generate(remaining_digits: str, previous_letters: List[str]):
            if len(remaining_digits) == 0:
                result.append("".join(previous_letters))
            else:
                for char in key_lookup[remaining_digits[0]]:
                    new_letters = previous_letters[::]
                    new_letters.append(char)
                    generate(remaining_digits[1:], new_letters)

        if len(digits) > 0:
            generate(digits, [])

        return result
