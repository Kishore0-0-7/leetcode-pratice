import math
class Solution(object):
    def isPerfectSquare(self, num):
        a=int(math.sqrt(num))
        return ((a*a)==num)
        