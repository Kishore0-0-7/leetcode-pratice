class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        g={0:[],1:[],2:[]}
        for x in nums:
            g[x%3].append(x)
        for r in g:
            g[r].sort(reverse=True)
        ans=0
        if len(g[0])>=3:
            ans=max(ans,sum(g[0][:3]))
        if len(g[1])>=3:
            ans=max(ans,sum(g[1][:3]))
        if len(g[2])>=3:
            ans=max(ans,sum(g[2][:3]))
        if g[0] and g[1] and g[2]:
            ans=max(ans,g[0][0]+g[1][0]+g[2][0])
        return ans
            