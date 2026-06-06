class Solution(object):
    def countElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums=list(set(nums))
        n=len(nums)
        if  n<=k:
            return 0
        return n-k
        