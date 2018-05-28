class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle)==0:
            return 0
        p1,p2 = 0,0 
        while p1<len(haystack) and p2<len(needle):
            if haystack[p1] == needle[p2]:
                p2 +=1
            p1+=1
            if p2 > len(needle):
                return p1-p2
        return -1

if __name__ == '__main__':
	s = Solution()
	print(s.strStr('hello','ll'))