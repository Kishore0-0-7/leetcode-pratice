class Solution(object):
    def constructTransformedArray(self, nums):
        n = len(nums)
        res = [0] * n
        for i in range(n):
            res[i] = nums[(i + nums[i]) % n]
        return res