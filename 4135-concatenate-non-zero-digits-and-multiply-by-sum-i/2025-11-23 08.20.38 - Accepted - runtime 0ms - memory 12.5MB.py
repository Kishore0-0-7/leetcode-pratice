class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=str(n).replace('0','')
        l=list(int(x) for x in s)
        if not s:
            return 0
        return int(s)*sum(l)