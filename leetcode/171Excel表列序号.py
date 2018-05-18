#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 14:32
# @Author  : DR
# @File    : 171Excel表列序号.py
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 注意：这里减去的是64 而不是65 因为A为65
        result = 0
        i = len(s)-1
        j = 1
        while i >= 0:
            result += (ord(s[i]) - 64)*j
            i -= 1
            j *= 26
        return result