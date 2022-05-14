from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def helper_l(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = l + ((r - l) >> 1)
                if nums[m] < target:
                    l = m + 1
                elif nums[m] == target:
                    r = m
                else:
                    r = m - 1
            return l if nums[l] == target else -1

        def helper_r(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = 1 + l + ((r - l) >> 1)
                if nums[m] < target:
                    l = m + 1
                elif nums[m] == target:
                    l = m
                else:
                    r = m - 1
            return r if nums[r] == target else -1

        if not nums: return [-1, -1]
        return [helper_l(nums, target), helper_r(nums, target)]


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchRange(nums = [5,7,7,8,8,10], target = 6))