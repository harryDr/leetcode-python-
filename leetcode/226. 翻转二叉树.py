#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 13:45
# @Author  : DR
# @File    : 226. 翻转二叉树.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def invertTree(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		# 交换左右子节点的值
		if not root:
			return None
		if root.left != None or root.right != None:
			root.left, root.right = root.right, root.left
			self.invertTree(root.left)
			self.invertTree(root.right)
		return root
