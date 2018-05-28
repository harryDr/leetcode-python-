#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 14:42
# @Author  : DR
# @File    : 121. 买卖股票的最佳时机.py

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #目的是找出序列中的最大差值 必须是后一个值减去前一个值
        #从前往后存入最小的值 不是最小就看差值是否最大 最大就存入
        if len(prices) == 0:
            return 0
        result = 0
        min_n = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < min_n:
                min_n = prices[i]
            else:
                if result < prices[i]- min_n:
                    result = prices[i]-min_n
        return result