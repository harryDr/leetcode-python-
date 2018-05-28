#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 16:08
# @Author  : DR
# @File    : 263. 丑数.py
class Solution(object):
	def isUgly(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		# 递归
		if num < 0:
			return False
		if num == 1:
			return True
		while num >= 2 and num % 2 == 0:
			num = num / 2
		while num >= 3 and num % 3 == 0:
			num = num / 3
		while num >= 5 and num % 5 == 0:
			num = num / 5
		return num == 1
