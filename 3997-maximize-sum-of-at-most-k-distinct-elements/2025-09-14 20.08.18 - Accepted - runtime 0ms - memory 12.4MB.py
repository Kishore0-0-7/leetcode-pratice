class Solution(object):
    def maxKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num=set(nums)
        lst=list(num)
        lst.sort(reverse=True)
        if len(num) >= k:
            return lst[:k]
        else:
            return lst