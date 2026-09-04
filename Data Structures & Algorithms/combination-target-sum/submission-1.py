class Solution:
    def combinationSum(self, nums, target):

        res = []
        path = []

        def dfs(start, target):

            if target == 0:
                res.append(path.copy())
                return

            if target < 0:
                return

            for i in range(start, len(nums)):

                path.append(nums[i])

                dfs(i, target - nums[i])

                path.pop()

        dfs(0, target)

        return res