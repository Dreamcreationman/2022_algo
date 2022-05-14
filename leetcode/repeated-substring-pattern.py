class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # https://leetcode-cn.com/problems/repeated-substring-pattern/
        return s in (s + s)[1:-1]

    def repeatedSubstringPattern_two(self, s: str) -> bool:
        # https://leetcode-cn.com/problems/repeated-substring-pattern/
        return self.strStr((s + s)[1:-1], s) != -1

    def getNext(self, b):
        if len(b) == 1: return [-1]
        nextArr = [-1, 0]
        i = 2
        cn = nextArr[i-1]
        while i < len(b):
            if b[cn] == b[i-1]:
                cn += 1
                nextArr.append(cn)
                i += 1
            elif cn > 0:
                cn = nextArr[cn]
            else:
                nextArr.append(0)
                i += 1
        return nextArr

    def strStr(self, a , b):
        if not b: return 0
        i = j = 0
        nextArr = self.getNext(b)
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                i += 1
                j += 1
            elif j != 0:
                j = nextArr[j]
            else:
                i += 1
        return i -j if j == len(b) else -1