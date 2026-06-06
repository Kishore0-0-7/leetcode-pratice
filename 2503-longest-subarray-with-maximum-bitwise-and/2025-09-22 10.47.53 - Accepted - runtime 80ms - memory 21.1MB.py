class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=max(nums)
        a=0
        cnt=0
        for i in nums:
            if i==maxi:
                cnt+=1
            else:
                cnt=0
            a=max(cnt,a)
        return a