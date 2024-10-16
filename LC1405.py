class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        size_array = sorted([(a, 'a'),(b, 'b'),(c, 'c')])
        result_array = []

        while True:
            if len(result_array) < 2 and size_array[2][0] > 0:
                result_array.append(size_array[2][1])
                size_array[2] = (size_array[2][0] - 1, size_array[2][1])
                size_array.sort()
            elif len(result_array) >= 2 and size_array[2][1] == result_array[-1] and size_array[2][1] == result_array[-2] and size_array[1][0] > 0:
                result_array.append(size_array[1][1])
                size_array[1] = (size_array[1][0] - 1, size_array[1][1])
                size_array.sort()
            elif len(result_array) >= 2  and size_array[2][0] > 0 and (size_array[2][1] != result_array[-1] or size_array[2][1] != result_array[-2]):
                result_array.append(size_array[2][1])
                size_array[2] = (size_array[2][0] - 1, size_array[2][1])
                size_array.sort()
            else:
                return "".join(result_array)