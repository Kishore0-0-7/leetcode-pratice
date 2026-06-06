class Solution(object):
    def reverse(self, x):
        n=0
        if(x<0):
            n=-(int(str(x)[:0:-1]))
        else:
            n=int(str(x)[::-1])
        if(n>=-2**31 and n<=(2**31)-1):
            return n
        return 0