class Solution(object):
    def rotate(self, nums, k):
            n=len(nums)
            nums[:]=nums[-(k%n):]+nums[:-(k%n)]