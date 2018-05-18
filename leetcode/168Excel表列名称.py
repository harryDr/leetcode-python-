#coding=utf-8
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        #需要注意26时：26%26为0 也就是0为A 所以使用n-1  A的ASCII码为65
        result = ""
        while n != 0:
            result = chr((n-1)%26+65) + result   #这里不可以使用+= 因为先求出来的是最后的一位
            n = (n-1)/26
        return result