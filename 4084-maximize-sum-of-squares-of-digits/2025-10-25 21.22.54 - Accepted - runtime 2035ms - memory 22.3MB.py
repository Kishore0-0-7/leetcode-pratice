class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        d=(num,sum)
        if sum>9*num:
            return ""
        res=[]
        for i in range(num):
            di=min(9,sum)
            res.append(str(di))
            sum-=di
        return "".join(res)