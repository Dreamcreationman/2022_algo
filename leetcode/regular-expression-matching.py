import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.match(p, s) is not None and len(re.match(p, s).group()) == len(s)

    def regex(self, s, p, i, j):
        if i == len(s) and j == len(p):
            return True

        if i < len(s) and j >= len(p): return False

        if j + 1 < len(p) and p[j + 1] == '*':
            if i < len(s) and (s[i] == p[j] or p[j] == "."):
                return self.regex(s, p, i + 1, j) or self.regex(s, p, i + 1, j + 2) or self.regex(s, p, i, j + 2)
            else:
                return self.regex(s, p, i, j+2)
        if i < len(s) and (p[j] == "." or s[i] == p[j]):
            return self.regex(s, p, i + 1, j + 1)

        return False

    def isMatch_two(self, s: str, p: str) -> bool:
        return self.regex(s, p, 0, 0)

    def isMatch_dp(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        dp[len(s)][len(p)] = True
        i, j = len(s), len(p)
        while i >= 0:
            while j >= 0:
                if j + 1 < len(p) and p[j + 1] == '*':
                    if i < len(s) and (s[i] == p[j] or p[j] == "."):
                        dp[i][j] = dp[i + 1][j] or dp[i + 1][j + 2] or dp[i][j + 2]
                    else:
                        dp[i][j] = dp[i][j + 2]
                if i < len(s) and (p[j] == "." or s[i] == p[j]):
                    dp[i][j] = dp[i + 1][j + 1]
                j -= 1
            i -= 1
        return dp[0][0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.isMatch_dp("ab", ".*"))