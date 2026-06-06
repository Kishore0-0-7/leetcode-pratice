class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=sum(nums[::2])
        s-=sum(nums[1::2])
        return s