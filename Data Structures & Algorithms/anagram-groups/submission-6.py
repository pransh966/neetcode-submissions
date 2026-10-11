class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for word in strs:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            key = tuple(count)

            if key not in ans:
                ans[key] = []

            ans[key].append(word)

        return list(ans.values())