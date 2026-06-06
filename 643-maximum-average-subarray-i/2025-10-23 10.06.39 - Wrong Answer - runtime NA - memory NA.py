class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        m=0.
        for i in range(0,len(nums)-k+1):
            s=0.
            for j in range(k):
                s+=nums[i+j]
            m=max(m,s/k)
        return m