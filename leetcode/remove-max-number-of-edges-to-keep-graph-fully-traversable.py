from typing import List


class DSU:
    def __init__(self, n):
        self.root = {}
        for i in range(1, n + 1):
            self.root[i] = i

    def find(self, a):
        if self.root[a] == a:
            return a
        self.root[a] = self.find(self.root[a])
        return self.root[a]

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x is None or y is None or x == y: return
        self.root[x] = y


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # https://leetcode-cn.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/submissions/
        if not n or not edges: return 0
        alice = []
        bob = []
        both = []
        for edge in edges:
            if edge[0] == 1:
                alice.append(edge[1:])
            elif edge[0] == 2:
                bob.append(edge[1:])
            else:
                both.append(edge[1:])
        dsu = DSU(n)
        counterBoth = 0
        for a, b in both:
            if dsu.find(a) == dsu.find(b):
                continue
            dsu.union(a, b)
            counterBoth += 1

        counterAlice = 0
        counterBob = 0
        dsuAlice = deepcopy(dsu)
        dsuBob = deepcopy(dsu)
        for a, b in alice:
            if dsuAlice.find(a) == dsuAlice.find(b):
                continue
            dsuAlice.union(a, b)
            counterAlice += 1

        for a, b in bob:
            if dsuBob.find(a) == dsuBob.find(b):
                continue
            dsuBob.union(a, b)
            counterBob += 1

        if counterAlice + counterBoth != n - 1 or counterBoth + counterBob != n - 1:
            return -1
        else:
            return len(edges) + counterBoth - 2 * n + 2