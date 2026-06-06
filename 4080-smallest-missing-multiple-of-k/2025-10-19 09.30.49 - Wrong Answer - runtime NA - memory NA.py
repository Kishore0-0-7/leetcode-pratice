class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=k
        for i in range(1,len(nums)):
            if n not in nums:
                return n
            n=k*i
        return n+k