import math
class Solution(object):
    def isPerfectSquare(self, num):
        a=int(math.sqrt(num))
        if ((a*a)==num):
            return True
        return False
        