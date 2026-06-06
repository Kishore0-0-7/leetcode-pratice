class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        sum=0
        for i in triangle:
            sum+=min(i)
        return sum