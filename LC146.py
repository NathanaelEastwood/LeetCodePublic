
class LRUCache:
    def __init__(self, capacity: int):
        self.values_map = {}
        self.mru = None
        self.lru = None
        self.capacity = capacity
        self.current_count = 0
    def get(self, key: int) -> int:
        if self.values_map.get(key) is not None:
            cache_object = self.values_map[key]
            if cache_object == self.lru:
                self.mru = cache_object
                self.lru = cache_object.previous_node
            elif cache_object != self.mru:
                previous_node = cache_object.previous_node
                next_node = cache_object.next_node
                cache_object.next_node = self.mru
                cache_object.previous_node = self.lru
                self.mru.previous_node = cache_object
                self.lru.next_node = cache_object
                self.mru = cache_object
                previous_node.next_node = next_node
                next_node.previous_node = previous_node

            return cache_object.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.current_count == 0:
            cache_object = CacheObject(key, value)
            cache_object.previous_node, cache_object.next_node = cache_object, cache_object
            self.values_map[key] = cache_object
            self.current_count += 1
            self.mru = cache_object
            self.lru = cache_object
        elif self.values_map.get(key) is not None:
            cache_object = self.values_map[key]
            cache_object.val = value
            if cache_object == self.lru:
                self.mru = cache_object
                self.lru = cache_object.previous_node
            elif cache_object != self.mru:
                previous_node = cache_object.previous_node
                next_node = cache_object.next_node
                previous_node.next_node = next_node
                next_node.previous_node = previous_node
                cache_object.next_node, self.mru.previous_node = self.mru, cache_object
                cache_object.previous_node, self.lru.next_node = self.lru, cache_object
                self.mru = cache_object
        else:
            cache_object = CacheObject(key, value, self.mru, self.lru)
            self.mru.previous_node = cache_object
            self.lru.next_node = cache_object
            self.mru = cache_object
            self.values_map[key] = cache_object
            self.current_count += 1

        if self.current_count > self.capacity:
            node_to_remove = self.lru
            self.lru = node_to_remove.previous_node
            self.lru.next_node = self.mru
            self.mru.previous_node = self.lru
            self.values_map.pop(node_to_remove.key)
            self.current_count -= 1



class CacheObject:
    def __init__(self, key: int, val: int, next_node = None, previous_node = None):
        self.key = key
        self.val = val
        self.next_node = next_node
        self.previous_node = previous_node
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)