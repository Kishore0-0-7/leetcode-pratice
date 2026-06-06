class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        if need1==0 and need2==0:
            return 0
        ans=float('inf')
        for k in (0, min(need1,need2),max(need1,need2)):
            r1=max(0,need1-k)
            r2=max(0,need2-k)
            total=k*costBoth+r1*cost1+r2*cost2
            ans=min(ans,total)
        return ans