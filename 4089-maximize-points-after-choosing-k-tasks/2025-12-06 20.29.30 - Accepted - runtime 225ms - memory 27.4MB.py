class Solution(object):
    def maxPoints(self, technique1, technique2, k):
        """
        :type technique1: List[int]
        :type technique2: List[int]
        :type k: int
        :rtype: int
        """
        n=len(technique1)
        total=sum(technique2)
        g=[]
        for i in range(n):
            g.append(technique1[i]-technique2[i])
        g.sort(reverse=True)
        for i in range(k):
            total+=g[i]
        for i in range(k,n):
            if g[i]>0:
                total+=g[i]
        return total