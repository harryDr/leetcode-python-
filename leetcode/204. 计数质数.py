#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/28 14:17
# @Author  : DR
# @File    : 204. 计数质数.py

# 自己的方法 leetcode编译器会报错 但实际是没问题的
# for  else 是for中没有执行break才会执行else 否则不会执行else
# class Solution(object):
#     def countPrimes(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n < 3:
#             return 0
#         result = []
#         for x in range(2,n+1):
#             for y in range(2,x):
#                 if x % y == 0:
#                     break
#             else:
#                 result.append(x)
#         return len(result)

class Solution(object):
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        """循环的范围进行了缩小"""
        for i in range(2, int(n ** 0.5) + 1):
            """先判断是否已经变为false，同时从i*i开始进行遍历"""
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)