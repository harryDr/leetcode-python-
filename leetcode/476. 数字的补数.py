#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 16:31
# @Author  : DR
# @File    : 476. 数字的补数.py

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i , temp= 1 , num
        while temp:
            i = i << 1
            temp = temp >> 1
        return num ^ (i-1)