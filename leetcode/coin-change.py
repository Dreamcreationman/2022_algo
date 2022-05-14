from typing import List


class Solution:
    def process(self, coins, index, rest):
        if index == len(coins):
            return 1 if rest == 0 else 0
        num = 0
        res = []
        while num * coins[index] <= rest:
            res += self.process(coins, index + 1, rest - num * coins[index])
            num += 1
        return num

    def coinChange(self, coins: List[int], amount: int) -> int:
        # https://leetcode.cn/problems/coin-change/
        return self.process(coins, 0, amount)


if __name__ == '__main__':
    sol = Solution()
    print(sol.coinChange(coins = [1, 2, 5], amount = 11))