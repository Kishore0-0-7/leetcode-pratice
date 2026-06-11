class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans,flip=0,False
        for bit in nums:
            if bit==flip:
                ans+=1
                flip=not flip 
        return ans