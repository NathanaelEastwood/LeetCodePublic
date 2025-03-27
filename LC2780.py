from collections import defaultdict
from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        frequency_table = defaultdict(int)

        for num in nums:
            frequency_table[num] += 1

        dominant_index = max(frequency_table, key=frequency_table.get)
        right_hand_table = frequency_table.copy()
        left_hand_table = defaultdict(int)

        current_split_position = 0
        right_hand_table[nums[current_split_position]] -= 1
        left_hand_table[nums[current_split_position]] += 1
        current_split_position += 1

        while not (max(right_hand_table, key = right_hand_table.get) == right_hand_table[dominant_index] and max(left_hand_table, key = left_hand_table.get) == left_hand_table[dominant_index]):
            if current_split_position >= len(nums): return -1
            right_hand_table[nums[current_split_position]] -= 1
            left_hand_table[nums[current_split_position]] += 1
            current_split_position += 1

        return -1 if current_split_position == len(nums) else current_split_position