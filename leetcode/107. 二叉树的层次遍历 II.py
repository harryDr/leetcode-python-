#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 10:05
# @Author  : DR
# @File    : 107. 二叉树的层次遍历 II.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def levelOrderBottom(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		# 利用栈实现 栈中存储的是节点和当前的层级
		# 先存入右节点 则会先处理左节点 这是栈的特性
		stack = [(root, 0)]
		res = []
		while stack:
			node, level = stack.pop()
			if node:
				if len(res) < (level + 1):
					res.insert(0, [])
				res[-(level + 1)].append(node.val)
				stack.append((node.right, level + 1))
				stack.append((node.left, level + 1))
		return res
