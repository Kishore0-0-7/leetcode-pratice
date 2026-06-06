class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums=[0,1]
        for i in range(2,n+1):
            nums.append(nums[i-1])
            nums.append(nums[i-1]+nums[i])
        return max(nums[:n+1])