#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        s = set()

        for pos in positions:
            s.add(pos[0])
            s.add(pos[0] + pos[1] - 1)

        s = sorted(list(s))
        smap = {val: idx for idx, val in enumerate(s)}
        ans = []
        res = 0
        height = [0] * len(s)

        for pos in positions:
            x, y = smap[pos[0]], smap[pos[0] + pos[1] - 1]
            max_cur = max(height[x: y+1])
            cur_res = max_cur + pos[1]

            for idx in range(x, y+1):
                height[idx] = cur_res

            res = max(cur_res, res)
            ans.append(res)
        return ans

