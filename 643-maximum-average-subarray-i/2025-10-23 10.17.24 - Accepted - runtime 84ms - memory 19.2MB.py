class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        ws=m=sum(nums[:k])
        for i in range(len(nums)-k):
            ws+=nums[i+k]-nums[i]
            m=max(m,ws)
        return m/float(k)