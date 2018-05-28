#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 14:40
# @Author  : DR
# @File    : 575. 分糖果.py

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        #种类最多为candies的一半 然后遍历candies看有多少个种类 求两者的最小值即为答案（要先排序）
        temp = 0
        max_num = len(candies)/2
        candies.sort()
        for i in range(len(candies)):
            if i==0 or candies[i] != candies[i-1]:
                temp += 1
        return min(temp,max_num)