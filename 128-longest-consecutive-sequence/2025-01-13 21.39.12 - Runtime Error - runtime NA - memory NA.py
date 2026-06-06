class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=1
        while i in nums:
            i+=1
        if i>max(nums):
            return i
        return i-1