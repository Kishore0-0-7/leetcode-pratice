class Solution(object):
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        xor=0
        for i in nums:
            xor^=i
        return xor==0 or len(nums)&1==0