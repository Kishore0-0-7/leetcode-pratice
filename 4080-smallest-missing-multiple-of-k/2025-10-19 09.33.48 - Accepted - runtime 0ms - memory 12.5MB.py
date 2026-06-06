class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=k
        while True:
            if n not in nums:
                return n
            n+=k