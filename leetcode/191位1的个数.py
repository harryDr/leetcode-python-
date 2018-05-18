#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 15:41
# @Author  : DR
# @File    : 191位1的个数.py
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #1011与1010与运算会减少一个1 运算一次减少一个1 知道n为0就运算了多少次
        count = 0
        while n:
            count += 1
            n = n & (n-1)
        return count