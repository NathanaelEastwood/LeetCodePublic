from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        total = 0
        currentRatingValue = 1
        i = 0
        for i in range(len(ratings) - 1):
            if ratings[i] <= ratings[i - 1] and ratings[i] <= ratings[i + 1]:
                currentRatingValue = 1
                total = total + currentRatingValue
            else:
                currentRatingValue += 1
                total = total + currentRatingValue
        if ratings[i] <= ratings[i - 1]:
            currentRatingValue = 1
            total = total + currentRatingValue
        else:
            currentRatingValue += 1
            total = total + currentRatingValue
        print(total)
        return total
