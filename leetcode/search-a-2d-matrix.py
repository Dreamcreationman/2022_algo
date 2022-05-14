from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # https://leetcode-cn.com/problems/search-a-2d-matrix
        if not matrix: return False
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j > -1:
            if target < matrix[i][j]:
                j -= 1
            elif target > matrix[i][j]:
                i += 1
            else:
                return True
        return False
