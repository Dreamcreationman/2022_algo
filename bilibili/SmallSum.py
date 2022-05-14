from typing import List


def merge(nums, l, m, r):
    res = []
    ans = 0
    i, j = l, m + 1
    while i <= m and j <= r:
        if nums[i] < nums[j]:
            ans += nums[i] * (r - j + 1)
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
    def countSmaller(self, nums: List[int]) -> List[int]:
        return divide(nums, 0, len(nums)-1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countSmaller([1, 3, 4, 2, 5]))
