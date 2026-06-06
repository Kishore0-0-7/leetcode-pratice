class Solution(object):
    def countElements(self, nums):
        mn = min(nums)
        mx = max(nums)
        return sum(1 for i in nums if mn < i < mx)