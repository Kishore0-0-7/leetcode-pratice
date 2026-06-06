class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        a=prices[0]
        p=0
        for i in range(1,len(prices)):
            if prices[i]<a:
                a=prices[i]
            if p<prices[i]-a:
                p=prices[i]-a
        return p