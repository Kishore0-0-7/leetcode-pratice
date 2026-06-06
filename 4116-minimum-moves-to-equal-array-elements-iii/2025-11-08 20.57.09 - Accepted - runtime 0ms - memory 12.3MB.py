class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=max(nums)
        t=m*len(nums)
        for i in nums:
            t-=i
        return t