from collections import deque


def bfs(node):
    if not node: return node
    q = deque()
    s = set()
    q.append(node)
    s.add(node)
    res = []
    while q:
        n = q.popleft()
        res.append(n.val)
        for subnode in n.next:
            if subnode not in s:
                s.add(subnode)
                q.append(subnode)
    return res