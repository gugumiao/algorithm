#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls = [ord(i)-97 for i in s]
        lp = [ord(i)-97 for i in p]
        hash = [0 for i in range(26)]
        m, n  = len(s), len(p)

        for i in range(n):
            hash[lp[i]] += 1

        l, r, count = 0, 0, 0
        res = []

        while r < m:
            hash[ls[r]] -= 1
            if hash[ls[r]] >= 0:
                count += 1

            if r > n - 1:
                hash[ls[l]] += 1
                if hash[ls[l]] > 0:
                    count -= 1
                l += 1
            if count == n:
                res.append(l)
            r += 1
        return res

