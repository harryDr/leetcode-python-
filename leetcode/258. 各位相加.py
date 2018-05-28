#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 16:58
# @Author  : DR
# @File    : 258. 各位相加.py
class Solution(object):
	def addDigits(self, num):
		"""
		:type num: int
		:rtype: int
		"""
		if num < 10:
			return num
		count = 0
		while num:
			count += num % 10
			if num / 10 == 0:
				if count < 10:
					return count
				else:
					num = count
					# 不要忘记吧count清零
					count = 0
					continue
			num /= 10
