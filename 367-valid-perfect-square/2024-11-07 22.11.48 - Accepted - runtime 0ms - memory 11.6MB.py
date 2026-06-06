import math
class Solution(object):
    def isPerfectSquare(self, num):
        a=int(math.sqrt(num))
        return (math.pow(a,2)==num)
        