class Solution(object):
    def smallestBalancedIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return -1
        ls,rp=0,1
        for i in nums:
            rp*=i
        rp/=nums[0]
        print(rp)
        ans=0
        for i in range(1,len(nums)):
            rp/=nums[i]
            ls+=nums[i-1]
            print(ls,rp)
            if ls==rp:
                return nums[i]
        return -1