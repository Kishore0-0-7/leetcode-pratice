class Solution(object):
    def maxCapacity(self, costs, capacity, budget):
        """
        :type costs: List[int]
        :type capacity: List[int]
        :type budget: int
        :rtype: int
        """
        machines=sorted(zip(costs,capacity))
        n=len(machines)
        best=[0]*n
        best[0]=machines[0][1]
        for i in range(1, n):
            best[i]=max(best[i-1],machines[i][1])
        ans=0
        for c,cap in machines:
            if c<budget:
                ans=max(ans,cap)
        for i in range(1,n):
            c2,cap2=machines[i]
            remaining=budget-c2-1
            if remaining<machines[0][0]:
                continue
            j=bisect.bisect_right(machines,(remaining,float('inf')),0,i)-1
            if j>=0:
                ans=max(ans,cap2+best[j])       
        return ans