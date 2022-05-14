from collections import defaultdict
from typing import List

class DSU:
    def __init__(self):
        self.root = {}

    def find(self, a):
        if a not in self.root:
            self.root[a] = a
            return a
        if self.root[a] == a: return a
        self.root[a] = self.find(self.root[a])
        return self.root[a]

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x == y: return
        self.root[x] = y


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        if not accounts: return
        dsu = DSU()
        mapping = {}
        for account in accounts:
            name, email, otherMail = account[0], account[1], account[2:]
            mapping[email] = name
            for mail in otherMail:
                mapping[mail] = name
                dsu.union(email, mail)
        res = defaultdict(list)
        for mail in mapping:
            account = dsu.find(mail)
            res[account].append(mail)

        return [[mapping[account]] + sorted(mails) for account, mails in res.items()]