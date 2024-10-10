class Solution:
    def isValid(self, s: str) -> bool:

        bracket_map = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        left_stack = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                left_stack.append(char)
            else:
                if len(left_stack) == 0 or left_stack.pop() != bracket_map[char]:
                    return False

        if len(left_stack) == 0:
            return True
        else:
            return False
