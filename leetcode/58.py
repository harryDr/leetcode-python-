#coding=utf-8
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)-1
        if len(s)==0:
            return 0
        count = 0
		#将字符串后的空格处理掉
        while l>0:
            if s[l] == ' ':
                s = s[:-1]
                l -= 1
            else:
                break
        for i in s[::-1]:
            if i == ' ':
                return count
            else:
                count += 1
        return count