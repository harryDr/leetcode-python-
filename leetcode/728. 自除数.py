#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 15:29
# @Author  : DR
# @File    : 728. 自除数.py

class Solution(object):
	def selfDividingNumbers(self, left, right):
		"""
		:type left: int
		:type right: int
		:rtype: List[int]
		"""
		# 暴力解法
		result = []
		i = left
		while i >= left and i <= right:
			# 判断自除数
			temp, flag = i, False
			while temp:
				if temp % 10 == 0:
					flag = False
					break
				if i % (temp % 10) == 0:
					flag = True
				else:
					flag = False
					break
				temp /= 10
			if flag == True:
				result.append(i)
			i += 1
		return result
