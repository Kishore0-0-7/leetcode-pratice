class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        sorted_digits = sorted(s)
        return (int(sorted_digits[-1]) * int(sorted_digits[-2]))