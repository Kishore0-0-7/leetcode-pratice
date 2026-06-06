class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxdif=-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                maxdif=max(maxdif,nums[j]-nums[i])
        return maxdif