from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        LetterMatch = True
        # check each letter of the string until you find one which doesn't match , then return that.
        NumberOfStrs = len(strs)
        CurrentLetterPos = 0
        outputString = ""
        while LetterMatch:
            currentLetterDict = {}
            if CurrentLetterPos < len(min(strs, key=len)):
                # Get all values for the given letter pos
                for i in range(NumberOfStrs):
                    if len(strs[i]) > 0:
                        currentLetterDict[i] = strs[i][CurrentLetterPos]
                # Test if all values of the given letter pos are equal
                LetterMatch = len(list(set(list(currentLetterDict.values())))) == 1
                CurrentLetterPos += 1
                if LetterMatch:
                    outputString = outputString + currentLetterDict[0]
            else:
                LetterMatch = False
        return outputString
