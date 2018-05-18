#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 14:32
# @Author  : DR
# @File    : 172阶乘后的零.py
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 要求末尾有多少个零，则该数应为x*10k 的形式等于x*（2k *5k）
        # 也就是求该数分解质因子后有几个5就行，：如1*2*3*4*5=1*2*3*2*2*5（里面有一个5）所以结果为1个0
        if n/5 < 5:
            return n/5
        else:
            return n/5 + self.trailingZeroes(n/5)