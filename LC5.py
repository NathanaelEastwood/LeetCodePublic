class Solution:
    def longestPalindrome(self, s: str) -> str:

        for i in range(len(s)):
            for j in range(i, len(s)):
                self.isPalindrome(s[i:j])


    def isPalindrome(self, s: str) -> bool:
        if len(s) % 2 == 0:
            for i in range (len(s)//2):
                if s[i] != s[-i]:
                    return False
        else:




        return "ab"