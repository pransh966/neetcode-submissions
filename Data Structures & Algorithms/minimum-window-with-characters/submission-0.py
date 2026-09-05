from collections import Counter

class Solution:
    def minWindow(self, s, t):

        need = Counter(t)

        left = 0
        count = 0
        answer = ""

        for right in range(len(s)):

            char = s[right]

            if char in need:

                if need[char] > 0:
                    count += 1

                need[char] -= 1

            while count == len(t):

                if answer == "" or right - left + 1 < len(answer):
                    answer = s[left:right + 1]

                char = s[left]

                if char in need:

                    need[char] += 1

                    if need[char] > 0:
                        count -= 1

                left += 1

        return answer
        