#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/28 16:04
# @Author  : DR
# @File    : 657. 判断路线成圈.py

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        flag = [0,0]
        for i in moves:
            if i == 'L':
                flag[0] -= 1
            if i == 'R':
                flag[0] += 1
            if i == 'U':
                flag[1] +=1
            if i == 'D':
                flag[1] -= 1
        if flag == [0,0]:
            return True
        else:
            return False