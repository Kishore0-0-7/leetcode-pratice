class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        x=0
        for i in nums:
            x^=i
        if x:
            return len(nums)
        return len(nums)-1 