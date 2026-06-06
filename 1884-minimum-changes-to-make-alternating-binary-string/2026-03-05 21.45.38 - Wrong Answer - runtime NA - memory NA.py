class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        c1=0
        if s[0]=='0':
            prev='1'
            c1=0
            for i in range(1,len(s)):
                if s[i]!=prev:
                    c1+=1
                prev='1' if prev=='0' else '0'
            prev='1'
        else:
            c1=0
            prev='0'
            for i in range(1,len(s)):
                if s[i]!=prev:
                    c1+=1
                prev='1' if prev=='0' else '0'
        return c1