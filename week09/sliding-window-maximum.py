#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res = []
        for i, n in enumerate(nums):
            if deque and deque[0] <= i - k:
                deque.popleft()
            while deque and n > nums[deque[-1]]:
                deque.pop()

            deque.append(i)
            if i >= k - 1:
                res.append(nums[deque[0]])
        return res

