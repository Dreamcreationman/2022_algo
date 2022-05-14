from typing import List


class Solution:
    def helper(self, nums, index, rest, dp):
        if index == len(nums) and rest == 0:
            dp[index][rest + 1000] = 1
            return 1
        if index == len(nums) and rest != 0:
            dp[index][rest + 1000] = 0
            return 0

        if dp[index][rest + 1000] != -1:
            return dp[index][rest + 1000]
        add = self.helper(nums, index + 1, rest - nums[index], dp)
        minus = self.helper(nums, index + 1, rest + nums[index], dp)
        dp[index][rest + 1000] = add + minus
        return dp[index][rest + 1000]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # https://leetcode-cn.com/problems/target-sum
        dp = [[-1] * (3000 + 1) for _ in range(21)]
        return self.helper(nums, 0, target, dp)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findTargetSumWays(nums = [1,1,1,1,1], target = 3))