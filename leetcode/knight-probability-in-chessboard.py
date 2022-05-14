class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # https://leetcode.cn/problems/knight-probability-in-chessboard/
        if row < 0 or column < 0 or row >= n or column >= n:
            return 0
        dp = []
        for i in range(k+1):
            dp.append([[0] * (n+2) for _ in range(n+2)])
        for i in range(0, n):
            for j in range(0, n):
                dp[0][i][j] = 1
        for rest in range(1, k+1):
            for i in range(0, n):
                for j in range(0, n):
                    dp[rest][i][j] =    dp[rest - 1][i + 2][j + 1] + \
                                        dp[rest - 1][i + 2][j - 1] + \
                                        dp[rest - 1][i - 2][j + 1] + \
                                        dp[rest - 1][i - 2][j - 1] + \
                                        dp[rest - 1][i + 1][j + 2] + \
                                        dp[rest - 1][i + 1][j - 2] + \
                                        dp[rest - 1][i - 1][j + 2] + \
                                        dp[rest - 1][i - 1][j - 2]
        return dp[k][row][column] / 8 ** k


if __name__ == '__main__':
    sol = Solution()
    print(sol.knightProbability(n = 8, k = 30, row = 6, column = 4))
