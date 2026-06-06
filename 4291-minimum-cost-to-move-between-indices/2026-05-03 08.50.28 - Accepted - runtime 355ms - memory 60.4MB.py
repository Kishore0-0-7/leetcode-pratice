class Solution(object):
    def minCost(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n=len(nums)
        c=[0]*n
        for i in range(n):
            l=float('inf')
            r=float('inf')
            if i>0:
                l=nums[i]-nums[i-1]
            if i<n-1:
                r=nums[i+1]-nums[i]
            if l<=r:
                c[i]=i-1
            else:
                c[i]=i+1
        fo=[0]*n
        for i in range(1,n):
            if c[i-1]==i:
                fo[i]=fo[i-1]+1
            else:
                fo[i]=fo[i-1]+(nums[i]-nums[i-1])
        ba=[0]*n
        for i in range(n-2,-1,-1):
            if c[i+1]==i:
                ba[i]=ba[i+1]+1
            else:
                ba[i]=ba[i+1]+(nums[i+1]-nums[i])
        res=[]
        for le,ri in queries:
            if le<ri:
                res.append(fo[ri]-fo[le])
            else:
                res.append(ba[ri]-ba[le])
        return res