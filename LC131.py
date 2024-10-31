from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        temp_partition = []
        def search(i):
            if i >= len(s):
                result.append(temp_partition.copy())
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]):
                    temp_partition.append(s[i:j+1])
                    search(j+1)
                    temp_partition.pop()

        search(0)
        return result

    def isPalindrome(self, s: str) -> bool:
        char_list = list(s)
        if len(char_list) % 2 == 0:
            mid_point = len(char_list) // 2
            for i in range(1, mid_point + 1):
                if char_list[mid_point + i - 1] != char_list[mid_point - i]:
                    return False
        else:
            mid_point = len(char_list) // 2
            for i in range(1, mid_point + 1):
                if char_list[mid_point + i] != char_list[mid_point - i]:
                    return False

        return True