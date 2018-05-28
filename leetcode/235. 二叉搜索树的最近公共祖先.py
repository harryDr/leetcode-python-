#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 14:02
# @Author  : DR
# @File    : 235. 二叉搜索树的最近公共祖先.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None or p == None or q == None:
            return None
        #分三种状态
        # 1.q p < root 2.q p >root 3.p>root q<root 不包含等号 等于root的时候就返回root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,q,p)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,q,p)
        else:
            return root