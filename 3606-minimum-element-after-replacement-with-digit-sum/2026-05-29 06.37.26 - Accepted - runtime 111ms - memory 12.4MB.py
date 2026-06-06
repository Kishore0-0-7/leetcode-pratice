class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(sum(int(d) for d in str(num)) for num in nums)