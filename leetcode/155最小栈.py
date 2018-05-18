#coding=utf-8
# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
# 
# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。
class MinStack(object):
	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.stock = []
		self.min_stock = []

	def push(self, x):
		"""
		:type x: int
		:rtype: void
		"""
		self.stock.append(x)
		if not self.min_stock or x <= self.min_stock[-1]:
			self.min_stock.append(x)

	def pop(self):
		"""
		:rtype: void
		"""
		if self.stock[-1] == self.min_stock[-1]:
			self.min_stock.pop()
		self.stock.pop()

	def top(self):
		"""
		:rtype: int
		"""
		return self.stock[-1]

	def getMin(self):
		"""
		:rtype: int
		"""
		return self.min_stock[-1]


		# Your MinStack object will be instantiated and called as such:
		# obj = MinStack()
		# obj.push(x)
		# obj.pop()
		# param_3 = obj.top()
		# param_4 = obj.getMin()