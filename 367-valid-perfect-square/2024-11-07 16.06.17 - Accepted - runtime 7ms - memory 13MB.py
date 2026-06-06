class Solution(object):
    def isPerfectSquare(self, num):
        for i in range(1,int((num**0.5)+1)):
            if(i*i==num):
                return True
        return False
        