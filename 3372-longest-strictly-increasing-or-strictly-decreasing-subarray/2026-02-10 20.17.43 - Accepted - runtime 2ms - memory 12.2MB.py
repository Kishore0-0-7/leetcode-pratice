class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx,c=1,1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                c+=1
            else:
                mx=max(mx,c)
                c=1
        mx=max(mx,c)
        c=1
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                c+=1
            else:
                mx=max(mx,c)
                c=1
        return max(mx,c)