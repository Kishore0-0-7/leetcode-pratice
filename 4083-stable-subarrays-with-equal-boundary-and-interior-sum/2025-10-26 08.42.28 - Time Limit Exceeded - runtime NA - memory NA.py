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
        for i in range(n):
            for j in range(i+2,n):
                ms=p[j]-p[i+1]
                if capacity[i]==capacity[j]==ms:
                    c+=1
        return c