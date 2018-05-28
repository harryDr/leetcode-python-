#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 11:06
# @Author  : DR
# @File    : 111. 二叉树的最小深度.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 使用递归
class Solution(object):
	def minDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0
		elif root.left == None and root.right == None:
			return 1
		else:
			l = self.minDepth(root.left)
			r = self.minDepth(root.right)
			# 此处需要加一个判断 因为在右为空的时候会少一个值
			# 例如1 2的树 题目要求输出2 不加判断会输出1
			if not l:
				return r + 1
			if not r:
				return l + 1
			return min(l, r) + 1
