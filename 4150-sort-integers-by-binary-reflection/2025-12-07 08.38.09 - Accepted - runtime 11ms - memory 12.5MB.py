class Solution(object):
    def sortByReflection(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def re(n):
            return int(bin(n)[2:][::-1],2)
        return sorted(nums,key=lambda x : (re(x),x))