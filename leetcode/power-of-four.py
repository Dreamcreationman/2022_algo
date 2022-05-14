class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # https://leetcode-cn.com/problems/power-of-four
        powerTwo = n > 0 and n & (n-1) == 0
        return powerTwo and  n & 0x55555555 != 0