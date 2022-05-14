class UnionFindSet:
    def __init__(self, data):
        self.elementMap = {}
        self.fatherMap = {}
        self.sizeMap = {}
        for d in data:
            self.elementMap[d] = d
            self.fatherMap[d] = d
            self.sizeMap[d] = 1

    def findHead(self, element):
        path = []
        while element != self.fatherMap[element]:
            path.append(element)
            element = self.fatherMap[element]
        while path:
            self.fatherMap[path.pop()] = element

    def isSameSet(self, a, b):
        if a in self.elementMap and b in self.elementMap:
            return self.findHead(self.elementMap[a]) == self.findHead(self.elementMap[b])
        return False

    def union(self, a, b):
        if a in self.elementMap and b in self.elementMap:
            aFather = self.findHead(a)
            bFather = self.findHead(b)
            if aFather != bFather:
                big = aFather if self.sizeMap[aFather] > self.sizeMap[bFather] else bFather
                small = bFather if big == aFather else aFather
                self.fatherMap[small] = big
                self.sizeMap[big] = self.sizeMap[small] + self.sizeMap[big]
                self.sizeMap.pop(small)


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