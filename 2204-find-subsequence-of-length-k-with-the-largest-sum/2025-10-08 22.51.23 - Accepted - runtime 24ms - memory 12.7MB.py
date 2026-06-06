class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        largest=sorted(nums)[-k:]
        result=[]
        for num in nums:
            if num in largest:
                result.append(num)
                largest.remove(num)
        return result