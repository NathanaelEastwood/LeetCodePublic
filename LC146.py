from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.cache_order = deque()
        self.capacity = capacity
        self.current_size = 0
    def get(self, key: int) -> int:

    def put(self, key: int, value: int) -> None:

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)