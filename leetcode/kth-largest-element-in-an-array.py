from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
        # q = []
        # for n in nums:
        #     heapq.heappush(q, n)
        # return heapq.nlargest(k, q)[-1]
        q = []
        i = 0
        while i < k:
            heapq.heappush(q, nums[i])
            i += 1
        while i < len(nums):
            if nums[i] > q[0]:
                heapq.heappop(q)
                heapq.heappush(q, nums[i])
            i += 1
        return q[0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findKthLargest([3,2,1,5,6,4], k = 2))