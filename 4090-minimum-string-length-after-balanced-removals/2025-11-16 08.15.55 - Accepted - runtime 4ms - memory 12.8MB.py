class Solution(object):
    def minLengthAfterRemovals(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_a=s.count('a')
        count_b=s.count('b')
        return abs(count_a-count_b)