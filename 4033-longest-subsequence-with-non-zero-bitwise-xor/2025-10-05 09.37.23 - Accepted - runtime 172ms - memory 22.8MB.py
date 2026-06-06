class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        x=0
        for i in nums:
            x^=i
        if x:
            return len(nums)
        all_zero=True
        for i in nums:
            if i!=0:
                all_zero=False
                break
        if all_zero:
            return 0
        return len(nums)-1 