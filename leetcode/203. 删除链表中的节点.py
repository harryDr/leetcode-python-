#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 15:23
# @Author  : DR
# @File    : 203. 删除链表中的节点.py
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def removeElements(self, head, val):
		"""
		使用双指针 并在头节点前加上一个节点 遇到一样的就删除
		:type head: ListNode
		:type val: int
		:rtype: ListNode
		"""
		per = ListNode(0)
		per.next = head
		cur = head
		cur_per = per
		while cur:
			if cur.val == val:
				cur_per.next = cur.next
			else:
				cur_per = cur_per.next
			cur = cur.next
		return per.next

	#可以将下一个节点复制到前一个节点删除下一个节点的方式（有点问题  需修改）
	# cur = head
	# while cur:
	# 	if cur.val == val:
	# 		cur = cur.next
	# 		cur.next = cur.next.next
	# 	cur = cur.next
	# return head

