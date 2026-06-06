class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        ans = 0
        for r in range(len(prices)):
            if r > 0 and prices[r] != prices[r - 1] - 1:
                l = r
            ans += (r - l + 1)
        return ans