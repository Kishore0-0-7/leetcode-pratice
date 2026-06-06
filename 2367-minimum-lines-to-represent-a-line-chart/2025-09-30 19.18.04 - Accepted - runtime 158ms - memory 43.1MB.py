class Solution(object):
    def minimumLines(self,stockPrices):
        """
        :type stockPrices: List[List[int]]
        :rtype: int
        """
        n=len(stockPrices)
        res=n-1
        stockPrices.sort()
        for i in range(1,n-1):
            a,b,c=stockPrices[i-1],stockPrices[i],stockPrices[i+1]
            if (b[0]-a[0])*(c[1]-b[1])==(c[0]-b[0])*(b[1]-a[1]):
                res-=1
        return res