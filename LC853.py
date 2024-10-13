from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # make an array which is the time it will take each car to reach the end
        tuple_array = []
        for i in range(len(position)):
            tuple_array.append((position[i], speed[i]))

        tuple_array.sort()

        time_array = []
        for i in range(len(tuple_array)):
            time_array.append((target - tuple_array[i][0]) / tuple_array[i][1])

        monotonic_ascending_stack_speed = []

        for i in time_array:
            while monotonic_ascending_stack_speed and monotonic_ascending_stack_speed[-1] <= i:
                monotonic_ascending_stack_speed.pop()
            monotonic_ascending_stack_speed.append(i)

        return len(monotonic_ascending_stack_speed)