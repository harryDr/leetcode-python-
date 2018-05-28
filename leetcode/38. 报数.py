#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 16:16
# @Author  : DR
# @File    : 38. 报数.py
class Solution(object):
	def countAndSay(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		# 需要知道前一个状态的数，使用递归
		# 从左到右有多少个重复的数
		s = '1'
		for i in range(n - 1):
			count = 1
			temp = []
			for index in range(1, len(s)):
				if s[index] == s[index - 1]:
					count += 1
				else:
					temp.append(str(count))
					temp.append(s[index - 1])
					count = 1
			temp.append(str(count))
			temp.append(s[-1])
			s = ''.join(temp)
		return s
