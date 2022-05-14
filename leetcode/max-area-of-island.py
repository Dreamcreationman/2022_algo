from typing import List


class Solution:
    def infection(self, board, i, j):
        if not 0 <= i < len(board) or not 0 <= j < len(board[i]) or board[i][j] != 1:
            return 0
        board[i][j] = 2
        return self.infection(board, i - 1, j) + self.infection(board, i + 1, j) + self.infection(board, i,
                                                                                                  j - 1) + self.infection(
            board, i, j + 1) + 1

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.infection(grid, i, j)
                    maxArea = max(maxArea, area)
        return maxArea