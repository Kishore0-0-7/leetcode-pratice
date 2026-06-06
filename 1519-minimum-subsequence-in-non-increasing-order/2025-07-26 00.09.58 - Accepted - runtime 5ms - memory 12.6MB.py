class Solution(object):
    def minSubsequence(self, nums):
        nums.sort(reverse = True)
        Sum = sum(nums)
        rSum = 0
        res = []
        for i in range(len(nums)):
            rSum += nums[i]
            res.append(nums[i])
            if(rSum > Sum - rSum):
                return res

        