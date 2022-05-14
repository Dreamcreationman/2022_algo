class Solution:
    def getNext(self, s):
        if len(s) == 1: return [-1]
        nextArr = [-1, 0]
        i = 2
        cn = nextArr[i - 1]
        while i < len(s):
            if s[cn] == s[i - 1]:
                cn += 1
                nextArr.append(cn)
                i += 1
            elif cn > 0:
                cn = nextArr[cn]
            else:
                nextArr.append(0)
                i += 1
        return nextArr

    def strStr(self, haystack: str, needle: str) -> int:
        # https://leetcode-cn.com/problems/implement-strstr/submissions/
        if not needle: return 0
        i = j = 0
        nextArr = self.getNext(needle)
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j != 0:
                j = nextArr[j]
            else:
                i += 1
        return i - j if j == len(needle) else -1
