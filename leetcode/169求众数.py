#coding=utf-8
class Solution(object):
	def majorityElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		#数组排序后存在众数 则中间的数必为众数
		nums.sort()
		return nums[len(nums) / 2]
