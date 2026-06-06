class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=0
        for i in nums:
            if (i%2==0):
                n|=i
        return n