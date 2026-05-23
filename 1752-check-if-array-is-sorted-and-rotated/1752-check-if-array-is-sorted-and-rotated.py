class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        drops=0
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                drops+=1
        if nums[-1]>nums[0]:
            drops+=1
        return drops<2