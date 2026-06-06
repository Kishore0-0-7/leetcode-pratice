class Solution(object):
    def reverse(self, x):
        if(x<0 and x>= -2**31):
            return -(int(str(x)[:0:-1]))
        elif(x>0 and x<=((2**31)-1)):
            return int(str(x)[::-1])
        return 0
        