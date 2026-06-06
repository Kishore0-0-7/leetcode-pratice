class Solution(object):
    def reverse(self, x):
        if(x<0):
            i=str(x)[:0:-1]
            n=int(i)
            return -(n)
        return int(str(x)[::-1])
        