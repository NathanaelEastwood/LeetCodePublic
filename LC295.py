import heapq

class MedianFinder:

    def __init__(self):
        self.small_heap = []
        self.large_heap = []
        heapq.heapify(self.large_heap)
        heapq.heapify(self.small_heap)
        self.current_median = 0
        self.total_count = 0

    def addNum(self, num: int) -> None:
        self.total_count += 1
        if num > self.current_median:
            heapq.heappush(self.large_heap, num)
        else:
            heapq.heappush(self.small_heap, -num)

        if abs(len(self.large_heap) - len(self.small_heap)) > 1:
            if len(self.large_heap) > len(self.small_heap):
                value = -heapq.heappop(self.large_heap)
                heapq.heappush(self.small_heap, value)
            else:
                value = -heapq.heappop(self.small_heap)
                heapq.heappush(self.large_heap, value)

        if self.total_count >= 2:
            if self.total_count % 2 == 0:
                self.current_median = (self.large_heap[0] - self.small_heap[0]) / 2
            elif len(self.large_heap) > len(self.small_heap):
                self.current_median = self.large_heap[0]
            else:
                self.current_median = -self.small_heap[0]
        else:
            self.current_median = num

    def findMedian(self) -> float:
        return self.current_median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()