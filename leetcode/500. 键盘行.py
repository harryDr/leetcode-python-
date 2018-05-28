#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 17:19
# @Author  : DR
# @File    : 500. 键盘行.py

class Solution(object):
	def findWords(self, words):
		"""
		:type words: List[str]
		:rtype: List[str]
		"""
		# 暴力解法 代码可以优化
		h1, h2, h3 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O',
					  'P'], ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K',
							 'L'], ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
		result = []
		for i in words:
			if i[0] in h1:
				flag = False
				for j in i:
					if j in h1:
						flag = True
					else:
						flag = False
						break
				if flag == True:
					result.append(i)

			if i[0] in h2:
				flag = False
				for j in i:
					if j in h2:
						flag = True
					else:
						flag = False
						break
				if flag == True:
					result.append(i)
			if i[0] in h3:
				flag = False
				for j in i:
					if j in h3:
						flag = True
					else:
						flag = False
						break
				if flag == True:
					result.append(i)
		return result