class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        for i,j in enumerate (nums):
            if i!=j:
                return j-1
            if j==len(nums)-1:
                return j+1
        