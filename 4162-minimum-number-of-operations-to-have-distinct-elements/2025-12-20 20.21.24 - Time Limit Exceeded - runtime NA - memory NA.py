class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        op=0
        n=len(nums)
        i=0
        while i<n:
            rem=nums[i:]
            if len(set(rem))==len(rem):
                break
            op+=1
            i+=3
        return op















      