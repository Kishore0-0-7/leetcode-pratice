class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(key=abs,reverse=True)
        s=nums[0]*nums[1]
        return abs(s*(10**5))