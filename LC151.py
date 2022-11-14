class Solution:
    def reverseWords(self, s: str) -> str:
        buffer = ""
        wordsArray = []
        for i in range(len(s)):
            if s[i] != " ":
                buffer = buffer + s[i]
            elif len(buffer) > 0 and s[i] == " ":
                wordsArray.append(buffer)
                buffer = ""
        if len(buffer) != 0:
            wordsArray.append(buffer)
        wordsArray.reverse()

        return ' '.join(wordsArray)

