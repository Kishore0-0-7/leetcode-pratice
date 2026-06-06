class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxdif=-1
        minso=nums[0]
        for i in range (1,len(nums)):
            if(nums[i]>minso):
                maxdif=max(maxdif,nums[i]-minso)
            else:
                minso=nums[i]
        return maxdif 