class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=str(abs(n))
        rer=s[::-1]
        n_rev=int(rer)
        return abs(n-n_rev)
        
        