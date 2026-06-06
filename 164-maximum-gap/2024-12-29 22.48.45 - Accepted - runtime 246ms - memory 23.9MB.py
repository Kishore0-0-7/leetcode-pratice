class Solution(object):
    def maximumGap(self, nums):
        nums.sort()
        l=[]
        if len(nums)<2:
            return 0
        else:
            for i in range(len(nums)-1):
                dif=nums[i+1]-nums[i]
                l.append(dif)
            return max(l)
        