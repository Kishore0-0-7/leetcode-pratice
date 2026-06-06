class Solution(object):
    def largestEven(self, s):
        """
        :type s: str
        :rtype: str
        """
        lt=s.rfind('2')
        if lt==-1:
            return ""
        return s[:lt+1]