class Solution(object):
    def missingNumber(self, nums):
        xa=0
        xn=0
        for i in range(len(nums)+1):
            xa^=i
        for i in nums:
            xn^=i
        return xa^xn