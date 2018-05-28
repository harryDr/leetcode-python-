#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 11:15
# @Author  : DR
# @File    : 389. 找不同.py

class Solution(object):
	def findTheDifference(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""
		# 两个字符串加起来只有一个字符时单独的。。利用异或运算
		result = 0
		for i in range(len(s)):
			result = result ^ (ord(s[i]) - ord('a'))
		for j in range(len(t)):
			result = result ^ (ord(t[j]) - ord('a'))
		return chr(result + ord('a'))
