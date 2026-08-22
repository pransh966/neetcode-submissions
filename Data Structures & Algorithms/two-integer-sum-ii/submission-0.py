class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            reqsum = numbers[left] + numbers[right]

            if reqsum > target:
                right -= 1

            elif reqsum < target:
                left += 1

            elif reqsum == target:
                return [left + 1, right + 1]