from collections import deque
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        current_left_hand = deque()

        for i in range(len(tokens)):
            if tokens[i] == '+':
                current_left_hand.append(current_left_hand.pop() + current_left_hand.pop())
            elif tokens[i] == '-':
                right_hand = current_left_hand.pop()
                left_hand = current_left_hand.pop()
                current_left_hand.append(left_hand - right_hand)
            elif tokens[i] == '*':
                current_left_hand.append(current_left_hand.pop() * current_left_hand.pop())
            elif tokens[i] == '/':
                divisor = current_left_hand.pop()
                target = current_left_hand.pop()
                current_left_hand.append(int(target / divisor))
            else:
                current_left_hand.append(int(tokens[i]))

        return current_left_hand.pop()

