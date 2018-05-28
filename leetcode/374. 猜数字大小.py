#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 17:25
# @Author  : DR
# @File    : 374. 猜数字大小.py

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
	def guessNumber(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		# 使用二分查找 不然超出时间限制 （关于界限的问题）
		if n == 1:
			return 1
		l, r = 1, n
		while l <= r:
			mid = (l + r) / 2
			if guess(mid) == 0:
				return mid
			if guess(mid) == -1:
				r = mid - 1
			if guess(mid) == 1:
				l = mid + 1

