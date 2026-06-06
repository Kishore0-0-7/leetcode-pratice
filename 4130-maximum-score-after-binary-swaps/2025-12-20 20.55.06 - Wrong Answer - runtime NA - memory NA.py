class Solution(object):
    def maximumScore(self, nums, s):
        """
        :type nums: List[int]
        :type s: str
        :rtype: int
        """
        b=0
        sc=0
        for i in range(len(nums)):
            b=max(b,nums[i])
            if s[i]=="1":
                sc+=b
                b=0
        return sc