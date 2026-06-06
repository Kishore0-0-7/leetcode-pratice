class Solution(object):
    def minimumPrefixLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=len(nums)-1
        while i>0 and nums[i-1]<nums[i]:
            # print(nums[i],nums[i-1]<nums[i])
            i-=1
        return i