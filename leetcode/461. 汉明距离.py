#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 16:09
# @Author  : DR
# @File    : 461. 汉明距离.py

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #使用异或求出不同的值  使用&求出二进制中有多少个1
        result = 0
        temp = x ^ y
        while temp:
            result += 1
            temp = temp & (temp-1)
        return result