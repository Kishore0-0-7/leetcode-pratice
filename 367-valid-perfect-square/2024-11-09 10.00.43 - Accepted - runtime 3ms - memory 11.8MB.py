import math
class Solution(object):
    def isPerfectSquare(self, num):
        a=0
        while a*a<=num:
            a+=1
        s=a-1
        return (s*s==num)