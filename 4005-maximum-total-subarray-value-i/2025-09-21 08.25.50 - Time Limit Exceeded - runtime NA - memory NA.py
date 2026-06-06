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
            for j in range (i,n):
                subarr=nums[i:j+1]
                cur=max(subarr)-min(subarr)
                maxi=max(maxi,cur)
        return maxi*k