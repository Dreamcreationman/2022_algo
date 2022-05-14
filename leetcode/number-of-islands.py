from typing import List

class Solution:
    def infection(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != "1": return
        grid[i][j] = "2"
        self.infection(grid, i+1, j)
        self.infection(grid, i-1, j)
        self.infection(grid, i, j-1)
        self.infection(grid, i, j+1)

    def numIslands(self, grid: List[List[str]]) -> int:
        # https://leetcode-cn.com/problems/number-of-islands/submissions/
        res = 0
        if not grid or not grid[0]: return res
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    self.infection(grid, i, j)
        return res


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    sol = Solution()
    print(sol.numIslands(grid))