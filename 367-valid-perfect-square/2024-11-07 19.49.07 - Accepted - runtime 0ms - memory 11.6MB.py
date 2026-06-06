import math
class Solution(object):
    def isPerfectSquare(self, num):
        a=int(math.sqrt(num))
        if (math.pow(a,2)==num):
            return True
        return False
        