class Solution(object):
    def isPerfectSquare(self, num):
        f=False
        for i in range(1,int((num**0.5)+1)):
            if(i*i==num):
                f=True
        return f
        