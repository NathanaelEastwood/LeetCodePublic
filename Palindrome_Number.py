
class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringInput = str(x)
        revStringInput = stringInput[::-1]
        if stringInput == revStringInput:
            return True
        else:
            return False
