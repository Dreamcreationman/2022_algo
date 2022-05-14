from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        https://leetcode-cn.com/problems/surrounded-regions
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return board
        m, n = len(board), len(board[0])

        def dfs(i, j):
            if not 0 <= i < n or not 0 <= j < m or board[i][j] != 'O':
                return
            board[i][j] = "A"
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for i in range(n):
            dfs(0, i)
            dfs(m-1, i)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        return board


if __name__ == '__main__':
    sol = Solution()
    print(sol.solve(board=[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))