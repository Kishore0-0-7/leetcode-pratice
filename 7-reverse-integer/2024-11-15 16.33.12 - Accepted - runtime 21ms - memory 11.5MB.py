import math
class Solution(object):
    def reverse(self, x):
        n=0
        if(x<0):
            n=x*-1
            n=int(str(n)[::-1])
            n=-(n)
        else:
            n=int(str(x)[::-1])
        m=math.pow(2,31)
        if(n>=-m and n<=m-1):
            return n
        return 0