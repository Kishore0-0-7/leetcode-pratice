class Solution(object):
    def firstMissingPositive(self, nums):
        i=1
        while(i in nums):
            i+=1
        return i