class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n=len(colors)
        md=0

        for i in range(n-1,-1,-1):
            if colors[i]!=colors[0]:
                md=i
                break
        for i in range(n):
            if colors[i]!=colors[n-1]:
                md=max(md,n-i-1)
                break
        return md