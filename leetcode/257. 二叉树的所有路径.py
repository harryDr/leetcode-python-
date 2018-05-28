#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 15:21
# @Author  : DR
# @File    : 257. 二叉树的所有路径.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def binaryTreePaths(self, root):
		"""
		:type root: TreeNode
		:rtype: List[str]
		"""
		# 使用dfs深度优先遍历 从顶点开始依次向下直到路劲中的所有都被访问 再回到顶点
		result = []

		def singalPath(root, path):
			if root.left == None and root.right == None:
				result.append(path)
			if root.left != None:
				singalPath(root.left, path + '->' + str(root.left.val))
			if root.right != None:
				singalPath(root.right, path + '->' + str(root.right.val))

		if not root:
			return result
		singalPath(root, str(root.val) + '')
		return result

