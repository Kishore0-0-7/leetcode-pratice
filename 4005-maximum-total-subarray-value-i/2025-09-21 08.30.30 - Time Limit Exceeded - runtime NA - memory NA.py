class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        maxi=0
        for i in range(n):
            curmax=nums[i]
            curmin=nums[i]
            for j in range (i,n):
                curmin=min(curmin,nums[j])
                curmax=max(curmax,nums[j])
                cur=curmax-curmin
                maxi=max(maxi,cur)
        return maxi*k