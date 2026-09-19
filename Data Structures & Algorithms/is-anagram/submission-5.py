class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map = {}

        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1

        for char in t:
            if char not in hash_map:
                return False

            hash_map[char] -= 1

        for count in hash_map.values():
            if count != 0:
                return False

        return True