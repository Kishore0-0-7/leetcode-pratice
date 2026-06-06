class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=float('inf')
        for num in nums:
            t=0
            for v in str(num):
                t+=int(v)
            ans=min(ans,t)
        return ans