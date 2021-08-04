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
        ar, br = self.find(a), self.find(b)
        if ar == br:
            return
        else:
            self.p[ar] = br
            self.size -= 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        ocean = 0
        uf = UnionFind(n*m)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "0":
                    ocean += 1
                else:
                    if i+1 < n and grid[i+1][j] == "1":
                        uf.union(i*m+j, (i+1)*m+j)
                    if j+1 < m and grid[i][j+1] == "1":
                        uf.union(i*m+j, i*m+(j+1))

        return uf.size - ocean

