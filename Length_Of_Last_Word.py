class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        outputLen = 0
        firstLetterFound = False
        lastLetterFound = False
        while not firstLetterFound:
            if s[i] != " ":
                outputLen += 1
                firstLetterFound = True
            i -= 1
        while not lastLetterFound and i >= 0:
            if s[i] != " ":
                outputLen += 1
            else:
                lastLetterFound = True
            i -= 1
        return outputLen
