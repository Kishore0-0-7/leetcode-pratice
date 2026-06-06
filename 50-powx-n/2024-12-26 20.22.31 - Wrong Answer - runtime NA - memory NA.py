class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        a=float(x)
        if (n<0):
            a=1/(a*x)
            n+=1
        else:
            for i in range (n-1):
                a=a*x
        return a

        
        