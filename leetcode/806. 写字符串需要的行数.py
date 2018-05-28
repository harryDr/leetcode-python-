#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 14:50
# @Author  : DR
# @File    : 806. 写字符串需要的行数.py

class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        #就是记录两个值累加
        col,row = 1,0 #i记录第几行 j记录这行的位置（>100换行）
        for i in S:
            if row + widths[ord(i)-ord('a')] > 100:
                col += 1
                row = widths[ord(i)-ord('a')]
            else:
                row += widths[ord(i)-ord('a')]
        return [col,row]