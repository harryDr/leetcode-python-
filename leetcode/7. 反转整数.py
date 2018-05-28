#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 17:23
# @Author  : DR
# @File    : 7. 反转整数.py
class Solution(object):
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		# 范围是0x7fffffff和-0x80000000
		y = x if x > 0 else -x
		z = 0
		while y > 0:
			z = z * 10 + y % 10
			y /= 10
		z = z if x > 0 else -z
		if z > 0x7fffffff or z < -0x80000000:
			return 0
		else:
			return z
