class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        i=1
        while i in nums or -i in nums:
            i+=1
        if i>max(nums):
            return i
        return i-1