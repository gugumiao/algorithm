#!/usr/bin/env python
# encoding: utf-8

import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.hmax = []
        self.hmin = []

    def addNum(self, num: int) -> None:
        if len(self.hmax) == len(self.hmin):
            heapq.heappush(self.hmin, -heapq.heappushpop(self.hmax, -num))
        else:
            heapq.heappush(self.hmax, -heapq.heappushpop(self.hmin, num))

    def findMedian(self) -> float:
        if len(self.hmin) == len(self.hmax):
            return (-self.hmax[0] + self.hmin[0]) / 2
        else:
            return self.hmin[0]

