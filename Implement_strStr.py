class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(needle) <= len(haystack):
            for element in range(0, len(haystack)):
                if needle[0] == haystack[element]:
                    i = 0
                    while element + i < len(haystack) and needle[i] == haystack[element + i]:
                        if i+1 == len(needle):
                            return element
                        else:
                            i = i + 1
        return -1
