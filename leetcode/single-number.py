from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # https://leetcode-cn.com/problems/single-number/
        a = 0
        for n in nums:
            a = a ^ n
        return a

    def singleNumber_ii(self, nums: List[int]) -> int:
        # https://leetcode-cn.com/problems/single-number-ii/
        ans = 0
        for i in range(32):
            total = sum((n >> i) & 1 for n in nums)
            if total % 3 == 1:
                ans = ans | (1 << i) if i != 31 else ans - (1 << i)
        return ans

    def singleNumber_iii(self, nums: List[int]) -> int:
        # https://leetcode-cn.com/problems/single-number-iii/
        a = 0
        for n in nums:
            a ^= n
        ringhtOne = a & (~a + 1)
        '''提取不为0的数最右侧的1：一个数与上(自己取反+1)'''
        b = 0
        for n in nums:
            if (n & ringhtOne) == 0:
                b ^= n
        return b, a ^ b


if __name__ == '__main__':
    a = [2,2, 2, 1, 1,1, -3]
    sol = Solution()
    print(sol.singleNumber_ii(a))