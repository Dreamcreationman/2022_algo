from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        # https://leetcode-cn.com/problems/sort-colors/
        Do not return anything, modify nums in-place instead.
        """
        l, r = -1, len(nums)
        p = 0
        while p != r:
            if nums[p] < 1:
                l += 1
                nums[p], nums[l] = nums[l], nums[p]
                p += 1
            elif nums[p] == 1:
                p += 1
            else:
                r -= 1
                nums[p], nums[r] = nums[r], nums[p]


