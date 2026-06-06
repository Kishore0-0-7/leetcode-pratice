class Solution(object):
    def firstMissingPositive(self, nums):
        i,a=1,1
        nums=set(nums)
        while(a):
            if i in nums:
                i+=1
            else:
                a=0   
        return i