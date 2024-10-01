from typing import List
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        map = {}
        for i in range(len(arr)):
            if map.get(arr[i] % k) is None:
                map[arr[i] % k] = 1
            else:
                map[arr[i] % k] += 1
        for key in map:
            if (map.get(k-key) is None or map[k - key] < 0 or map[key] < 0) and key != 0:
                return False
            elif map[key] == 0 or key == 0:
                continue
            else:
                if k - key == key and map[key] % 2 != 0:
                    return False
                map[k - key] -= map[key]
                map[key] = 0

        return True
