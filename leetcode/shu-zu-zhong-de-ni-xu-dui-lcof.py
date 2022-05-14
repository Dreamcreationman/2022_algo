from typing import List


def merge(nums, l, m, r):
    res = []
    ans = 0
    i, j = l, m + 1
    while i <= m and j <= r:
        if nums[i] > nums[j]:
            ans += (r - j + 1)
            res.append(nums[i])
            i += 1
        else:
            res.append(nums[j])
            j += 1
    if i <= m:
        res.extend(nums[i:m + 1])
    else:
        res.extend(nums[j:r + 1])
    for i in range(len(res)):
        nums[l + i] = res[i]
    return ans


def divide(nums, l, r):
    if l == r:
        return 0
    m = l + ((r - l) >> 1)
    return divide(nums, l, m) + divide(nums, m + 1, r) + merge(nums, l, m, r)


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
        if nums is None: return
        if len(nums) < 2: return 0
        return divide(nums, 0, len(nums)-1)