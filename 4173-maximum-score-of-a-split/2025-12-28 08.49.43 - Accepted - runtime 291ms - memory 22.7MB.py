class Solution(object):
    def maximumScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        sm=nums[-1]
        s=[0]*n
        s[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            sm=min(sm,nums[i])
            s[i]=sm
        ps=0
        ms=float('-inf')
        for i in range(n-1):
            ps+=nums[i]
            score=ps-s[i+1]
            ms=max(ms,score)
        return ms