
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}

        left = 0
        max_freq = 0
        result = 0

        for right in range(len(s)):

            # Add character to window
            count[s[right]] = count.get(s[right], 0) + 1

            # Maximum frequency in the window
            max_freq = max(max_freq, count[s[right]])

            # If too many replacements are required
            while (right - left + 1) - max_freq > k:

                count[s[left]] -= 1
                left += 1

            # Current window is valid
            result = max(result, right - left + 1)

        return result
        

        