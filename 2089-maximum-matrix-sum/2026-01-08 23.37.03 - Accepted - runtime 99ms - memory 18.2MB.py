class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        ts=0
        neg=0
        ma=float('inf')
        for row in matrix:
            for v in row:
                if v<0:
                    neg+=1
                av=abs(v)
                ts+=av
                ma=min(ma,av)
        return ts if neg%2==0 else ts-2*ma