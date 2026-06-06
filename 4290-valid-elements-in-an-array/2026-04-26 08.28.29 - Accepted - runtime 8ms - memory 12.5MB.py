class Solution(object):
    def findValidElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        if n<=2:
            return nums
        lm=[0]*n
        rm=[0]*n
        lm[0]=float('-inf')
        rm[n-1]=float('-inf')
        for i in range(1,n):
            lm[i]=max(lm[i-1],nums[i-1])
        for i in range(n-2,-1,-1):
            rm[i]=max(rm[i+1],nums[i+1])
        result=[]
        for i in range(n):
            if nums[i]>lm[i] or nums[i]>rm[i]:
                result.append(nums[i])
        return result