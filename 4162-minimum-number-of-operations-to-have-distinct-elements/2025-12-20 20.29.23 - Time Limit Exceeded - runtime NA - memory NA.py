class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==len(set(nums)):
            return 0
        op=0
        start=0
        n=len(nums)
        while start<n:
            op+=1
            start+=3
            r=nums[start:]
            if len(r)==len(set(r)):
                break
        return op
            