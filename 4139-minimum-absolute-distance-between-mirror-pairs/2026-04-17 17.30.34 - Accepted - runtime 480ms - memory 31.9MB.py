class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def reverse(x):
            return int(str(x)[::-1])
        mp={}
        ans=float('inf')
        for i in range(len(nums)):
            if nums[i] in mp:
                ans=min(ans,i-mp[nums[i]])
            mp[reverse(nums[i])]=i
        return ans if ans!=float('inf') else -1