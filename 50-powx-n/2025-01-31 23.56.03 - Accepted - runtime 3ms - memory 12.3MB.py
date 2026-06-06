class Solution(object):
    def myPow(self, x, n):
        if (n<0):
            n=-n
            x=1/x
        p=1
        while n!= 0:
            if n&1!=0:
                p*= x
            x*=x
            n=n>>1
        return p

        
        