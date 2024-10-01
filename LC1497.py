from typing import List
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        map = {}
        for i in range(len(arr)):
            if map.get(arr[i] % k) is None:
                map[arr[i] % k] = 1
            else:
                map[arr[i] % k] += 1
        for key in list(map.keys()):
            if (map.get(key) != map.get(k-key) and key != 0) or (key == k-key) % 2 != 0:
                return False
            elif map.get(key) is not None and map.get(key-k) is not None:
                map.pop(key)
                map.pop(k-key)
        return True
