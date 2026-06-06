from math import sqrt

class Solution(object):
    def minOperations(self, k):
        v = int(sqrt(k))
        return v + (k - 1) // v - 1