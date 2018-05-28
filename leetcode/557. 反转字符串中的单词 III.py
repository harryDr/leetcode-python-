#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/28 15:50
# @Author  : DR
# @File    : 557. 反转字符串中的单词 III.py

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
		# [::-1] 用来翻转   split()以空格划分存入list ' '.join()拼接字符串以空格为连接符
        return ' '.join(x[::-1] for x in s.split())
