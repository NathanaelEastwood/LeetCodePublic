class Solution:
    def minLength(self, s: str) -> int:
        substitution_made = True
        list = [c for c in s]
        while substitution_made:
            substitution_made = False
            i = 0
            for i in range(len(list)):
                if not substitution_made:
                    current_char = list[i]
                    previous_char = list[i-1] if i != 0 else "Z"

                    if (current_char == "B" and previous_char == "A") or (current_char == "D" and previous_char == "C"):
                        list.pop(i)
                        list.pop(i-1)
                        substitution_made = True

        return len(list)