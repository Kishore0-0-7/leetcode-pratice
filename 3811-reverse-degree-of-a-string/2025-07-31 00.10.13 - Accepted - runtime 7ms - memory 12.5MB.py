class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        for i in range(len(s)):
            value=ord(s[i])-ord('a')
            ans+=(i+1)*(26-value)
        return ans