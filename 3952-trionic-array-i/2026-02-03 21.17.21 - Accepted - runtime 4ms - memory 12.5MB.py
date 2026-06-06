class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        isIncreasing=isDecreasing=lastIncre=False
        ind=0

        while ind+1<n and nums[ind]<nums[ind+1]:
            isIncreasing=True
            ind+=1

        while ind+1<n and nums[ind]>nums[ind+1]:
            isDecreasing=True
            ind+=1

        while ind+1<n and nums[ind]<nums[ind+1]:
            lastIncre=True
            ind+=1

        return isIncreasing and isDecreasing and lastIncre and ind==n-1