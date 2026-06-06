class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort()
        i=len(cost)-3
        buy=sum(cost)
        free=0
        while i>=0:
            free+=cost[i]
            i-=3
        return buy-free