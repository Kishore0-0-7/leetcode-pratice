class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        c1=0
        c2=0
        for i in range(len(s)):
            e1='0' if i&1==0 else '1'
            e2='1' if i&1==0 else '0'

            if s[i]!=e1: c1+=1
            if s[i]!=e2: c2+=1
            
        return min(c1,c2)