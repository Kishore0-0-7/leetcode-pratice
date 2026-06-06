class Solution(object):
    def maxCapacity(self, costs, capacity, budget):
        """
        :type costs: List[int]
        :type capacity: List[int]
        :type budget: int
        :rtype: int
        """
        n=len(costs)
        machines=list(zip(costs,capacity))
        machines.sort()
        ans=0
        for c,cap in machines:
            if c<budget:
                ans=max(ans,cap)
        l,r=0,n-1
        while l<r:
            total_cost=machines[l][0]+machines[r][0]
            if total_cost<budget:
                total_capacity=machines[l][1]+machines[r][1]
                ans=max(ans, total_capacity)
                l+=1
            else:
                r-=1
        return ans