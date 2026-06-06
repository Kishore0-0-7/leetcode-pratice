class Solution(object):
    def countStableSubarrays(self, capacity):
        """
        :type capacity: List[int]
        :rtype: int
        """
        n=len(capacity)
        p=[0]*(n+1)
        for i in range(n):
            p[i+1]=p[i]+capacity[i]
        c=0
        seen=defaultdict(int)
        for i in range(n):
            if i>=2:
                k=(capacity[i],p[i]-capacity[i])
                c+=seen[k]
            if i+1<=n-1:
                k=(capacity[i],p[i+1])
                seen[k]+=1
        return c