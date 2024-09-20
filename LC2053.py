from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        result = []

        for i in range(len(arr)):
            new_result = [arr[i], arr.count(arr[i])]
            result.append(new_result)

        # sort into dictionary where key is "a" and value is count

        current_distinct_string = 1
        for value in result:
            if value[1] == 1 and current_distinct_string == k:
                return value[0]
            elif value[1] == 1:
                current_distinct_string += 1

        return ""
