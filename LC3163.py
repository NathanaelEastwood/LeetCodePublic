class Solution:
    def compressedString(self, word: str) -> str:
        current_run = 1
        result = []
        for s in range(0, len(word) - 1):
            if word[s] == word[s+1] and current_run < 9:
                current_run += 1
            else:
                result.append(f"{current_run}")
                result.append(word[s])
                current_run = 1

        if len(word) > 1 and word[-1] == word[-2]:
            result.append(f"{current_run}")
            result.append(word[-1])
        else:
            current_run = 1
            result.append(f"{current_run}")
            result.append(word[-1])

        return "".join(result)
