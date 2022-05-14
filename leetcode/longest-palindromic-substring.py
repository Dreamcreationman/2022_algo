import math

class Solution:
    def expand(self, s, l, r):
        L, R = l, r
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1

    def longestPalindrome(self, s: str) -> str:
        # https://leetcode.cn/problems/longest-palindromic-substring/
        if not s: return
        start = end = 0
        for i in range(len(s)):
            c1 = self.expand(s, i, i)
            c2 = self.expand(s, i, i+1)
            c = max(c1, c2)
            if c > (end - start):
                start  = i - (c -1) // 2
                end  =i + c // 2
        return s[start:end + 1]

    def process(self, s, i, j):
        if i > j: return ""
        if i == j: return s[i]
        if s[i] == s[j] and len(self.process(s, i+1, j-1)) == j - i - 1:
            return s[i:j+1]
        else:
            s1 = self.process(s, i+1, j)
            s2 = self.process(s, i, j-1)
            return s1 if len(s1) > len(s2) else s2

    def longestPalindrome_cur(self, s: str) -> str:
        if not s: return
        return self.process(s, 0, len(s)-1)

    def longestPalindrome_dp(self, s: str) -> str:
        if not s: return
        n = len(s)
        dp = [[""] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = s[i]
        i = n - 2
        j = i + 1
        while i >= 0:
            while j < n:
                if s[i] == s[j] and len(dp[i + 1][j - 1]) == j - i - 1:
                    dp[i][j] = s[i:j + 1]
                else:
                    dp[i][j] = dp[i + 1][j] if len(dp[i + 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]
                j += 1
            i -= 1
            j = i + 1
        return dp[0][n - 1]

    def longestPalindrome_dp2(self, s: str) -> str:
        if not s: return
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        i = n - 1
        j = 0
        maxLen = start = end = 0
        while i >= 0:
            while j < n:
                if i > j:
                    dp[i][j] = True
                elif i == j:
                    dp[i][j] = True
                elif s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if maxLen < (j - i):
                        maxLen = j - i
                        start = i
                        end = j
                j += 1
            i -= 1
            j = 0
        return s[start:end+1] if maxLen != 0 else s[0]

    def longestPalindrome(self, s: str) -> str:
        if not s: return
        s = "#" + "#".join(s) + "#"
        radius = [0] * len(s)
        R = C = -1
        maxi = -math.inf
        center = -1
        for i in range(len(s)):
            radius[i] = 1 if i > R else min(radius[2 * C - i], R - i)
            while i + radius[i] < len(s) and i - radius[i] > -1:
                if s[i + radius[i]] == s[i - radius[i]]:
                    radius[i] += 1
                else: break
            if i + radius[i] > R:
                R = i + radius[i]
                C = i
            if radius[i] > maxi:
                maxi = radius[i]
                center = i
        return s[center - maxi + 1: center + maxi ].replace("#", "")


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome_dp2("cbbd"))