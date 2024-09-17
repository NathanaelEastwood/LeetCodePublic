from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        combine = s1 + " " + s2
        combine = combine.split()
        result_dict = {}
        result = []
        for i in range(len(combine)):
            if combine[i] not in result_dict:
                result_dict[combine[i]] = 1
            elif result_dict.get(combine[i]) > 0:
                result_dict[combine[i]] += 1

        for key, value in result_dict.items():
            if value == 1:
                result.append(key)

        return result
