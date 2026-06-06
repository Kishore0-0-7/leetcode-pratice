class Solution(object):
    def findPeakElement(self, nums):
        mx=max(nums)
        return nums.index(mx)
        