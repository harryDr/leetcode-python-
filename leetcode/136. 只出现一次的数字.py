#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 16:17
# @Author  : DR
# @File    : 136. 只出现一次的数字.py

class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		# 使用异或来解决问题 其他方式时间或空间复杂度不能满足要求
		temp = nums[0]
		if len(nums) == 0:
			return 0
		for i in range(1, len(nums)):
			temp = temp ^ nums[i]
		return temp

