class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = maxCount = 0 
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                maxCount = max(count, maxCount)
                count = 0          
        return max(count, maxCount)
        