#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 16:14
# @Author  : DR
# @File    : 198. 打家劫舍.py
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划问题 n个数组的最大值划分为：n-1个的最大值 和n-2个的最大值+数组最后一个值 两者的最大值
        #f(0) = nums[0]
        #f(1) = max(num[0], num[1])
        #f(k) = max( f(k-2) + nums[k], f(k-1) )
        if not nums:
            return 0
        if len(nums)<3:
            return max(nums)
        else:
            j = 2
            nums[1] = max(nums[0],nums[1])
            while j < len(nums):
                nums[j] = max(nums[j-1],nums[j-2]+nums[j])
                j += 1
            return nums[-1]