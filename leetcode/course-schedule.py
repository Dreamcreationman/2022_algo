from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # https://leetcode-cn.com/problems/course-schedule/
        in_node = [0] * numCourses
        next = [[] for _ in range(numCourses)]
        zero_in = deque()
        for pre, then in prerequisites:
            in_node[pre] += 1
            next[then].append(pre)
        for idx, inn in enumerate(in_node):
            if inn == 0:
                zero_in.append(idx)
        while zero_in:
            pre = zero_in.popleft()
            numCourses -= 1
            for nex in next[pre]:
                if nex != pre:
                    in_node[nex] -= 1
                    if not in_node[nex]: zero_in.append(nex)
        return not numCourses

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # https://leetcode-cn.com/problems/course-schedule-ii/
        in_node = [0] * numCourses
        res = []
        zero_in = deque()
        for pre, then in prerequisites:
            in_node[pre] += 1
        for idx, inn in enumerate(in_node):
            if inn == 0:
                zero_in.append(idx)
        while zero_in:
            deletenode = zero_in.popleft()
            res.append(deletenode)
            for pre, then in prerequisites:
                if then == deletenode and then != pre:
                    in_node[pre] -= 1
                    if in_node[pre] == 0:
                        zero_in.append(pre)
        return res if len(res) == numCourses else []


if __name__ == '__main__':
    sol = Solution()
    print(sol.canFinish(numCourses=20, prerequisites=[[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))
