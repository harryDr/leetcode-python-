#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 16:55
# @Author  : DR
# @File    : 404. 左叶子之和.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def sumOfLeftLeaves(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		# BFS 层级遍历来获取每层左叶子节点的和
		# 判断的规则是如果某一节点的左子节点存在，并且该左子节点没有左右孙子节点，则该左子节点就是左叶子节点。
		# 当满足上述规则时就加上该左子节点值，不满足就添加非空子节点到队列中，直到队列为空。
		stock = [root]
		result = 0
		if not root:
			return result
		while stock:
			node = stock.pop()
			if node.left:
				# 可以直接判断当前节点的左节点是否是叶子节点
				if node.left.left == None and node.left.right == None:
					result += node.left.val
				stock.append(node.left)
			if node.right:
				stock.append(node.right)
		return result
