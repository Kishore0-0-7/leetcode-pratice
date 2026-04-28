class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=int(-99999)
        n=len(nums)
        sum=0
        for i in range(n):
            cur=nums[i]
            sum=max(cur,sum+cur)
            maxi=max(maxi,sum)
        return maxi
    