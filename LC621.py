import collections
import heapq
from typing import List
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # as this is a greedy problem, we want to prioritise the task that can be done, that has the largest number of remaining instances
        # we want to keep data on how long ago each task ran, and how many instances of this task there are.
        # (side note, why does this keep reminding me of LRU Cache?, it definitely has a lot of similarities)

        # setup our priority queue with the priority being the number of operations
        available_tasks = PriorityQueue()
        # our on_cooldown_tasks is a dequeue of tasks on cooldown. When we can remove one to replace it into the priority queue, we can pop it out (new items need to be appendedleft)
        # the value is a tuple (remaining_count, value) e.g. (2, 'D')
        on_cooldown_tasks = deque()
        # generate an initial cooldown in our dequeue
        for i in range(n):
            on_cooldown_tasks.appendleft((0, None))

        task_types = Counter(tasks)

        for task_key in task_types.keys():
            available_tasks.enqueue(task_key, -task_types[task_key])

        result = 0
        operation = 0
        while operation != len(tasks):
            result += 1
            # our cycle goes - take the highest element out of the priority queue if it exists
            task = available_tasks.dequeue()
            if task and task[0] < 0:
                # if it does, we subtract 1 from its priority/count, and place it on the left of the cooldown
                operation += 1
                on_cooldown_tasks.appendleft((task[0] + 1, task[-1]))
            else:
                # if it doesn't exist, we just add a None value to the left of our cooldown list
                on_cooldown_tasks.appendleft((0, None))

            # then we remove the topmost (right) element of our cooldown queue and replace it into our priority map
            off_cooldown = on_cooldown_tasks.pop()
            if off_cooldown[0] and off_cooldown[0] < 0:
                available_tasks.enqueue(off_cooldown[1], off_cooldown[0])

        return result

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def enqueue(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1
    def dequeue(self):
        if len(self._queue) > 0:
            return heapq.heappop(self._queue)
        else:
            return None
    def peek(self):
        return self._queue[0][-1]
    def count(self):
        return len(self._queue)


