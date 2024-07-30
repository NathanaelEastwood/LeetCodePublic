class Solution:
    def minimumDeletions(self, s: str) -> int:
        # find already correct characters
        correct_starts = 0
        correct_ends = -1
        while correct_starts < len(s) and s[correct_starts] == "a":
            correct_starts += 1
        while -correct_ends < len(s) and s[correct_ends] == "b":
            correct_ends -= 1

        if correct_ends == -1:
            manipulable_values = s[correct_starts:]
        else:
            correct_ends += 1
            manipulable_values = s[correct_starts:correct_ends]

        current_value = 0
        encountered_b = 0

        for i in range(len(manipulable_values)):
            if manipulable_values[i] == "a":
                current_value = min(current_value + 1, encountered_b)
            else:
                encountered_b += 1

        return current_value