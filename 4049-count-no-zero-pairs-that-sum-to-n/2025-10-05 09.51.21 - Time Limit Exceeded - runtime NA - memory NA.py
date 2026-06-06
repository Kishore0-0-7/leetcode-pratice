class Solution(object):
    def countNoZeroPairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        t=n
        c=0
        for a in range(1,t):
            if "0" in str(a):
                continue
            b=t-a
            if "0" not in str(b):
                c+=1
        return c