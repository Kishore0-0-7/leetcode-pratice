class Solution(object):
    def minimumOperations(self, nums):
        num=set(nums)
        if 0 in nums:
            return len(num)-1
        return len(num)    