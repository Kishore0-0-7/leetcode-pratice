class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        n=len(nums)
        curr=0
        for i in range(n):
            if nums[i]==0:
                curr+=1
            else:
                ans+=curr*(curr+1)//2
                curr=0
        ans+=curr*(curr+1)//2
        return ans