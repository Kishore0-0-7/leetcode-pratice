class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort() 
        n = len(nums)
        p1 = nums[0] * nums[1]
        p2 = nums[-1] * nums[-2]
        res = p2 - p1
        return res