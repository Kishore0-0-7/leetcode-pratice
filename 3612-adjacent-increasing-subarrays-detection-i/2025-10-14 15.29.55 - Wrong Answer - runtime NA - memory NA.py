class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        c=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                c+=1
            else:
                c=1
            if c>=k:
                return True
        return False