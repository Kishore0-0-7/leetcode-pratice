class Solution(object):
    def minOperations(self, k):
        """
        :type k: int
        :rtype: int
        """
        v = sqrt(k)
        return int(v + (k - 1) // v - 1)