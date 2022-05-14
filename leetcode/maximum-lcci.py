class Solution:
    def maximum(self, a: int, b: int) -> int:
        # https://leetcode-cn.com/problems/maximum-lcci
        res = a - b
        sca = (res >> 63) & 1
        scb = 1 ^ sca
        return a * scb + b * sca