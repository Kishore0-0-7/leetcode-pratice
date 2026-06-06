import math
class Solution(object):
    def isPerfectSquare(self, num):
        return (math.pow(int(math.sqrt(num)),2)==num)
        