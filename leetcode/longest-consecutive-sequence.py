from typing import List


class DSU:
    def __init__(self, data):
        self.root = {}
        self.size = {}
        for d in data:
            self.root[d] = d
            self.size[d] = 1

    def find(self, a):
        if a not in self.root: return
        if self.root[a] == a:
            return a
        self.root[a] = self.find(self.root[a])
        return self.root[a]

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x is None or y is None or x == y: return
        if self.size[x] > self.size[y]:
            self.root[y] = x
            self.size[x] = max(self.size[x], self.size[y] + 1)
        else:
            self.root[x] = y


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = list(set(nums))
        dsu = DSU(nums)
        for n in nums:
            dsu.union(n, n - 1)
            dsu.union(n, n + 1)
        counter = defaultdict(int)
        for n in nums:
            counter[dsu.find(n)] += 1
        return max(counter.values())