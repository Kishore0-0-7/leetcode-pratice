class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=str(n).replace('0','')
        l=list(int(x) for x in s)
        return int(s)*sum(l)