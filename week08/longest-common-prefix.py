#!/usr/bin/env python
# encoding: utf-8

import re


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        x = strs[0]
        for i in range(1, len(strs)):
            if len(strs[i]) < len(x):
                x = strs[i]

        for s in strs:
            while not re.match('^' + x, s):
                x = x[:-1]
                if not x:
                    return ""
        return x

