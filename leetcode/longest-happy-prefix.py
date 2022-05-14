class Solution:
    def longestPrefix(self, s: str) -> str:
        # https://leetcode-cn.com/problems/longest-happy-prefix
        n = len(s)
        fail = [-1] * n
        for i in range(1, n):
            j = fail[i - 1]
            while j != -1 and s[j + 1] != s[i]:
                j = fail[j]
            if s[j + 1] == s[i]:
                fail[i] = j + 1

        return s[:fail[-1] + 1]

    def longestPrefix_two(self, s: str) -> str:
        if len(s) == 1: return ""
        nextArr = [0]
        i = 1
        cn = nextArr[i-1]
        while i < len(s):
            if s[cn] == s[i]:
                cn += 1
                nextArr.append(cn)
                i += 1
            elif cn > 0:
                cn = nextArr[cn-1]
            else:
                nextArr.append(0)
                i += 1
        return s[:nextArr[-1]]


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPrefix_two("level"))