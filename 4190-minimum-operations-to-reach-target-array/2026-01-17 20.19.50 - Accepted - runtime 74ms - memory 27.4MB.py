class Solution(object):
    def minOperations(self, nums, target):
        """
        :type nums: List[int]
        :type target: List[int]
        :rtype: int
        """
        # n=len(nums)
        # ops=0
        # for i in range(n):
        #     if nums[i]!=target[i]:
        #         if i==0 or nums[i]!=nums[i-1] or nums[i-1]==target[i-1]:
        #             ops+=1
        # return ops
        needed=set()
        for i in range(len(nums)):
            if nums[i]!=target[i]:
                needed.add(nums[i])
        return len(needed)