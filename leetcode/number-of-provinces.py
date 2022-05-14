from collections import defaultdict


class DSU:
    def __init__(self, data):
        self.root = {}
        for d in data:
            self.root[d] = d

    def find(self, a):
        if self.root[a] == a:
            return self.root[a]
        self.root[a] = self.find(self.root[a])
        return self.root[a]

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x is None or y is None or x == y: return
        self.root[x] = y


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        dsu = DSU([i for i in range(len(isConnected))])
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]:
                    dsu.union(i, j)
        counter = defaultdict(int)
        for i in range(len(isConnected)):
            counter[dsu.find(i)] += 1
        return len(set(counter.keys()))