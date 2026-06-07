class Solution(object):
    def sumOfGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        ans=0
        for i in range(max(1,n-k),n+k+1):
            if n&i==0:
                ans+=i
        return ans