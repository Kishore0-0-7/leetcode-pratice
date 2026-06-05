class Solution(object):
    def minimumOperations(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[1]*n
        m=1
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if nums[i]>=nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
                    m=max(m,dp[i])
        return n-m
