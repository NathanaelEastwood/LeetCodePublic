class Solution:
    def romanToInt(self, s: str) -> int:
        stringArray = list(s)
        roman_Values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        runningTotal = 0
        iter = 0
        while iter <= len(stringArray) - 1:
            if iter == len(stringArray) - 1:
                runningTotal = runningTotal + roman_Values[stringArray[iter]]
                break
            if roman_Values[stringArray[iter]] >= roman_Values[stringArray[iter + 1]]:
                runningTotal = runningTotal + roman_Values[stringArray[iter]]
                iter += 1
            else:
                runningTotal = runningTotal + (roman_Values[stringArray[iter + 1]] - roman_Values[stringArray[iter]])
                iter += 2
        print(runningTotal)
        return runningTotal


