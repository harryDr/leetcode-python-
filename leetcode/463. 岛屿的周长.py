#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/28 15:31
# @Author  : DR
# @File    : 463. 岛屿的周长.py

#暴力循环
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        col,row = len(grid),len(grid[0])
        for i in range(col):
            for j in range(row):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] == 0:
                        count += 1
                    if i == col-1 or grid[i+1][j] == 0:
                        count += 1
                    if j == 0 or grid[i][j-1] == 0:
                        count +=1
                    if j == row-1 or grid[i][j+1]==0:
                        count += 1
        return count

# 还可以使用1.遍历数组，如果是1则加上4（四条边）；
# 2.如果该位置是1并且它的左边是1的话，那么就抵消了两条边，则减2；
# 3.如果该位置是1并且它的上边是1的话，那么就抵消了两条边，则减2；
# 4.返回周长即可。