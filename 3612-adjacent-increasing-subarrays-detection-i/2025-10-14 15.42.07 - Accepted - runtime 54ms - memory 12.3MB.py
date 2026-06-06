class Solution(object):
    def isStrictlyIncreasing(self,nums,start,k):
        for i in range(start,start+k-1):
            if nums[i]>=nums[i+1]:
                return False
        return True
    def hasIncreasingSubarrays(self,nums,k):
        n=len(nums)
        if n < 2*k:
            return False
        for i in range(n-2*k+1):
            if self.isStrictlyIncreasing(nums,i,k) and self.isStrictlyIncreasing(nums,i+k,k):
                return True
        return False
