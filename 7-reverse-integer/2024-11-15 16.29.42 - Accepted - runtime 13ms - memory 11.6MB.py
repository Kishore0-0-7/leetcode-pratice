import math
class Solution(object):
    def reverse(self, x):
        m=math.pow(2,31)
        if(x<0):
            x=-(int(str(x*-1)[::-1]))
        else:
            x=int(str(x)[::-1])
        if(x>=-m and x<=m-1):
            return x
        return 0