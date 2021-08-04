#!/usr/bin/env python
# encoding: utf-8

class UnionFind:
    def __init__(self, n):
        self.size = n
        self.p = [i for i in range(n)]

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
            return self.p[x]
        return x

    def union(self, a, b):
        if self.connected(a, b):
            return
        ar, br = self.find(a), self.find(b)
        self.p[ar] = br
        self.size -= 1

    def connected(self, a, b):
        return self.find(a) == self.find(b)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(1001)
        for ai, bi in edges:
            if uf.connected(ai, bi):
                return [ai, bi]
            uf.union(ai, bi)

