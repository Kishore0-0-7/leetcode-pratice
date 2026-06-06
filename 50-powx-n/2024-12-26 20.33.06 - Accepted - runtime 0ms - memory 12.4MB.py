class Solution(object):
    def myPow(self, x, n):
        if (n<0):
            x=1/x
            n=-n
        p=1
        while n > 0:
            if n % 2 == 1:
                p *= x
            x =x*x
            n //= 2
        return p

        
        