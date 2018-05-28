#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 15:23
# @Author  : DR
# @File    : 202. 快乐数.py
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #satck用来存储平方和后的数据，一旦里面有重复，即不会出现快乐数（也就是跳出循环的标志）
        result = False
        count = 0
        stack = []
        while n:
            count += (n%10)*(n%10)
            if n/10 == 0:
                n = count
                if count == 1:
                    result = True
                    break
                if count in stack:
                    result = False
                    break
                else:
                    stack.append(count)
                count = 0
                continue
            n /= 10
        return result