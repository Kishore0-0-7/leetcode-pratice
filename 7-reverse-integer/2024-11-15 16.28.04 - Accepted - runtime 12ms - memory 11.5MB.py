import math
class Solution(object):
    def reverse(self, x):
        n,m=0,math.pow(2,31)
        if(x<0):
            n=-(int(str(x*-1)[::-1]))
        else:
            n=int(str(x)[::-1])
        if(n>=-m and n<=m-1):
            return n
        return 0