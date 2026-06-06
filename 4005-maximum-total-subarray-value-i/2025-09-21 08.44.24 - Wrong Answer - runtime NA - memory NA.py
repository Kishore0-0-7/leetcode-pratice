class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        gmax=max(nums)
        gmin=min(nums)
        diff=gmax-gmin
        if diff==0:
            return 0
        lmax=-1
        lmin=-1
        count=0
        for i in range(n):
            if nums[i]==gmax:
                lmax=i
            if nums[i]==gmin:
                lmin=i
            if lmax!=-1 and lmin!=-1:
                left=min(lmin,lmax)
                if i-k+1>=0:
                    count+=max(0,min(left,i-k+1)+1)
        return diff*count