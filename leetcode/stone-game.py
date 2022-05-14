from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # https://leetcode.cn/problems/stone-game
        if not piles: return False
        f = [[-1] * len(piles) for _ in range(len(piles))]
        s = [[-1] * len(piles) for _ in range(len(piles))]
        for i in range(len(piles)):
            for j in range(len(piles)):
                f[i][j] = piles[i]
                s[i][j] = 0
        row, col = 0, 1
        while col < len(piles):
            i = row
            j = col
            while i < len(piles) and j < len(piles):
                f[i][j] = max(piles[i] + s[i+1][j], piles[j] + s[i][j-1])
                s[i][j] = min(f[i+1][j], f[i][j-1])
                i += 1
                j += 1
            col += 1
        return f[0][len(piles)-1] > s[0][len(piles)-1]