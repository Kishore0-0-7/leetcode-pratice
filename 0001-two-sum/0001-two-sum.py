class Solution(object):
    def twoSum(self, nums, target):
        num_i={}
        for i in range (len(nums)):
            n=nums[i]
            sh=target-n
            if sh in num_i:
                return[num_i[sh],i]
            num_i[n]=i
        return[]