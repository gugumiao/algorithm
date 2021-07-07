#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        m = [[] for _ in range(numCourses)]
        n = [0] * numCourses
        for i, j in prerequisites:
            n[i] += 1
            m[j].append(i)
        ans = [i for i, j in enumerate(n) if not j]
        for i in ans:
            for j in m[i]:
                n[j] -= 1
                not n[j] and ans.append(j)
        return numCourses == len(ans) and ans or []

