class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        k=float('inf')
        for i in range(len(nums)):
            if nums[i]==target:
                k=min(k,i-start)
        return k