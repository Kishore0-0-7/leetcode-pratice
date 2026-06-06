class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        for i,num in enumerate (nums):
            if num>=target:
                return i
        return len(nums)
        