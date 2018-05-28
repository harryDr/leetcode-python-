class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s)==0):
            return 0
        l = len(s)-1
        sum = 0
        while l>=0:
            if s[l] == 'V':
                if l>0 and s[l-1] == 'I':
                    sum+=4
                    l-=1
                else:
                    sum+=5
            elif s[l] == 'X':
                if l>0 and s[l-1] == 'I':
                    sum+=9
                    l-=1
                else:
                    sum+=10
            elif s[l] == 'L':
                if l>0 and s[l-1] == 'X':
                    sum+=40
                    l-=1
                else:
                    sum+=50
            elif s[l] == 'C':
                if l>0 and s[l-1] == 'X':
                    sum+=90
                    l-=1
                else:
                    sum+=100
            elif s[l] == 'D':
                if l>0 and s[l-1] == 'C':
                    sum+=400
                    l-=1
                else:
                    sum+=500
            elif s[l] == 'M':
                if l>0 and s[l-1] == 'C':
                    sum+=900
                    l-=1
                else:
                    sum+=1000
            else:
                sum+=1
            l-=1
        return sum