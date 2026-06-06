class Solution(object):
    def myPow(self, x, n):
        if (n<0):
            x=1/x
            n=-n
        p=1
        for i in range (n):
            p=p*x
        return p

        
        