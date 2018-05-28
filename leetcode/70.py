#coding=utf-8
class Solution(object):
	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		# 斐波拉切数列
		# 递归法（自顶向下） 会超时 （可以优化）
		# if n == 1:
		#     return 1
		# elif n == 2:
		#     return 2
		# else:
		#     return self.climbStairs(n-1)+self.climbStairs(n-2)

		# 迭代 (自底向上)
		count, a, b = 0, 1, 2
		if n == 1:
			return 1
		elif n == 2:
			return 2
		else:
			for i in range(2, n):
				count = a + b
				a = b
				b = count
		return count