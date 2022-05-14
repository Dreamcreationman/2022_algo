from typing import List


class Solution:
    def merge(self, arr, l, m, r):
        res = []
        i, j = l, m + 1
        while i <= m and j <= r:
            if arr[i] <= arr[j]:
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j += 1
        if i <= m:
            res.extend(arr[i:m+1])
        elif j <= r:
            res.extend(arr[j:r+1])
        for i in range(len(res)):
            arr[l + i] = res[i]

    def divide(self, arr, l, r):
        if l == r: return
        m = l + ((r - l) >> 1)
        self.divide(arr, l, m)
        self.divide(arr, m + 1, r)
        self.merge(arr, l, m, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        # https://leetcode-cn.com/problems/sort-an-array/
        if not nums or len(nums) < 2: return nums
        self.divide(nums, 0, len(nums) - 1)
        return nums


if __name__ == '__main__':
    sol = Solution()
    print(sol.sortArray([5,2,3,1]))
