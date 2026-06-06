class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_val = min(nums)
        max_val = max(nums)
        diff = max_val - min_val
        reduced = diff - 2 * k
        return max(0, reduced)