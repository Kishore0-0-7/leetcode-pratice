class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum = 0
        for i, v in enumerate(nums):
            if n % (i+1) == 0:
                sum += v**2
        return sum