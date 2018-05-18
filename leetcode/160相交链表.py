#coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 两个指针分别指向两个链表 因为链表长度不同 不停循环指针
        # 直到两个指针指向相交的点或者是尾节点结束
        if headA == None or headB == None:
            return None
        pa,pb = headA,headB
        while pa is not pb:
            pa = headB if pa == None else pa.next
            pb = headA if pb == None else pb.next
        return pa