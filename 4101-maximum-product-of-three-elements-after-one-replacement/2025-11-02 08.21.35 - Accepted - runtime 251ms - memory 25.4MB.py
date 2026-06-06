class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(key=abs,reverse=True)
        return abs(nums[0]*nums[1]*(10**5))