class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        s="".join(ch for ch in str(n) if ch!='0')
        if not s:
            return 0
        ts=sum(int(x) for x in s)
        return int(s)*ts