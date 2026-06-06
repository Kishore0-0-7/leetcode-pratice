class Solution(object):
    def smallestBalancedIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n<=1:
            return -1
        ls=[0]*n
        ls[n-1]=math.log(nums[n-1])

        for i in range(n-2,-1,-1):
            ls[i]=ls[i+1]+math.log(nums[i])
        s=0
        
        for i in range(n):
            if i==n-1:
                rp=0
            else:
                rp=ls[i+1]
            if s>0 and abs(math.log(s)-rp)<1e-9:
                return i
            s+=nums[i]
        return -1