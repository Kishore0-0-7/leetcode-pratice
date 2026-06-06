class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==0:
            return 0
        left=[1]*n
        right=[1]*n
        for i in range(1,n):
            if nums[i]>=nums[i-1]:
                left[i]=left[i-1]+1
        for i in range(n-2,-1,-1):
            if nums[i]<=nums[i+1]:
                right[i]=right[i+1]+1
        mxl=max(left)
        for i in range(n):
            if i>0:
                mxl=max(mxl,left[i-1]+1)
            if i<n-1:
                mxl=max(mxl,right[i+1]+1)
            if i>0 and i<n-1 and nums[i-1]<=nums[i+1]:
                mxl=max(mxl,left[i-1]+right[i+1])
        return mxl
                