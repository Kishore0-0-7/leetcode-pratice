class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max=0
        start=prices[0]
        n=len(prices)
        for i in range(0,n):
            if start<prices[i]: 
                max+=prices[i]-start
            start=prices[i]
        return max