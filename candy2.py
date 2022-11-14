from typing import List
import math


class Solution:
    def candy(self, ratings: List[int]) -> int:
        smallestVal = min(ratings)
        centrePos = ratings.index(smallestVal)
        currentRatingPos = ratings.index(smallestVal)
        totalCandy = 0
        currentCandyRating = 1
        finishedRight = False
        # get the smallest value and the index of it. iterate through the numbers excluding the first and last
        # number. i does not denote the value of the array currently handled
        i = 1
        for i in range(len(ratings)):
            if len(ratings) > currentRatingPos + 1:  # are there values to the right or left
                if ratings[currentRatingPos] > ratings[currentRatingPos + 1]:  # is the right-hand neighbour smaller?
                    currentCandyRating = currentCandyRating + 1
            elif 0 <= currentRatingPos - 1:
                if ratings[currentRatingPos] > ratings[currentRatingPos - 1]:
                    currentCandyRating = currentCandyRating + 1
            else:
                currentCandyRating = currentCandyRating - 1
            totalCandy = totalCandy + currentCandyRating

            # defines the movement through the list below
            if len(ratings) == currentRatingPos + 1:
                currentRatingPos = centrePos
                currentCandyRating = 1
                finishedRight = True
            if len(ratings) > currentRatingPos + 1 and not finishedRight:
                currentRatingPos += 1
            elif 0 <= currentRatingPos - 1:
                currentRatingPos -= 1
        return totalCandy