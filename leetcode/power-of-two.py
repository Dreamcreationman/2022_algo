class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # https://leetcode-cn.com/problems/power-of-two/
        if n == 0: return False
        return n & (n-1) == 0