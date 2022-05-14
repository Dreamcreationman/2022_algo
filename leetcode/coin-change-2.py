from typing import List


class Solution:
    def process(self, coins, index, rest):
        if index == len(coins):
            return 1 if rest == 0 else 0
        num = 0
        res = 0
        while num * coins[index] <= rest:
            res += self.process(coins, index+1, rest - num * coins[index])
            num += 1
        return res

    def change(self, amount: int, coins: List[int]) -> int:
        return self.process(coins, 0, amount)

    def change_dp(self, amount: int, coins: List[int]) -> int:
        # https://leetcode.cn/problems/coin-change-2
        N =len(coins)
        dp = [[0] * (amount+1) for _ in range(N+1)]
        dp[N][0] = 1
        row = N-1
        while row >= 0:
            for i in range(amount+1):
                n = 0
                while n * coins[row] <= i:
                    dp[row][i] += dp[row+1][i-n * coins[row]]
                    n += 1
            row -= 1
        return dp[0][amount]

    def change_dp2(self, amount: int, coins: List[int]) -> int:
        # https://leetcode.cn/problems/coin-change-2
        N =len(coins)
        dp = [[0] * (amount+1) for _ in range(N+1)]
        dp[N][0] = 1
        row = N-1
        while row >= 0:
            for i in range(amount+1):
                dp[row][i] = dp[row+1][i]
                if i - coins[row] >= 0:
                    dp[row][i] += dp[row][i - coins[row]]
            row -= 1
        return dp[0][amount]


if __name__ == '__main__':
    sol = Solution()
    print(sol.change_dp2(500, [3,5,7,8,9,10,11]))