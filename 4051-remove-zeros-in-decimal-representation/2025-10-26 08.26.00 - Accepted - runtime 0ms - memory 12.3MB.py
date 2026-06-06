class Solution(object):
    def removeZeros(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int("".join(i for i in (str(n)) if i!="0"))