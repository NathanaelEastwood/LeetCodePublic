from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.vault = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vault[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.vault[key]
        l = 0
        r = len(values) - 1
        m = l + ((r - l) // 2)

        if r == -1:
            return ""


        while l <= r:
            if values[m][0] == timestamp:
                return values[m][1]
            elif values[m][0] <= timestamp:
                l = m + 1
            else:
                r = m - 1

            m = l + ((r - l) // 2)

        if values[m][0] > timestamp:
            return ""

        return values[m][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)