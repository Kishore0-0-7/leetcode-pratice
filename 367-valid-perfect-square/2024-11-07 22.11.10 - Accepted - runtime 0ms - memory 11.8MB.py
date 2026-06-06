import math
class Solution(object):
    def isPerfectSquare(self, num):
        a=int(num**0.5)
        return ((a*a)==num)
        