class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string_array = []
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isnumeric():
                cleaned_string_array.append(s[i])

        for i in range(len(cleaned_string_array)//2):
            if cleaned_string_array[i].lower() != cleaned_string_array[-i-1].lower():
                return False

        return True

