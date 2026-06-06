class Solution(object):
    def sortedSquares(self, nums):
        a=[i*i for i in nums]
        a.sort()
        return a
        