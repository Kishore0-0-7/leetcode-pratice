class Solution(object):
    def matrixSum(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        s=0
        for arr in nums:
            arr.sort()
        
        while nums[0]:
            m=0
            for arr in nums:
                n=arr.pop()
                m=max(m,n)
            s+=m
        return s