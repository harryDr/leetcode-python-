#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 10:27
# @Author  : DR
# @File    : 110. 平衡二叉树.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def isBalanced(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""

		def height(root):
			'''
			计算节点的高度
			'''
			if root == None:
				return 0
			else:
				l = height(root.left)
				r = height(root.right)
			return l + 1 if l > r else r + 1

		if root == None:
			return True
		else:
			l = height(root.left)
			r = height(root.right)
			if l > r + 1 or r > l + 1:
				return False
			else:
				return self.isBalanced(root.left) and self.isBalanced(root.right)
