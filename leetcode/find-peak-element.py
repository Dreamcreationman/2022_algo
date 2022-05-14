from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # https://leetcode-cn.com/problems/find-peak-element
        # 左神视频 1:51:00
        if nums is None: return
        if len(nums) < 2: return 0
        if nums[0] > nums[1]: return 0
        if nums[len(nums) - 1] > nums[len(nums) - 2]: return len(nums) - 1
        i, j = 0 , len(nums) - 1
        while i<= j:
            m = (i + j) // 2
            if nums[m+1] < nums[m] > nums[m-1]: return m
            elif nums[m] < nums[m+1]: i = m + 1
            else: j = m - 1
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.findPeakElement(nums = [1,2,1,3,5,6,4]))

"""
所以对于二分而言，不是只有有序才能使用二分，实际上只要二分后可以排除掉另一部分，那就可以使用二分

二分求中点的时候，直接m=(l+r) // 2有可能在大数组情况下溢出，所以我们通常写成 l + (r-l) // 2 或 l + (r-l) >> 1
"""