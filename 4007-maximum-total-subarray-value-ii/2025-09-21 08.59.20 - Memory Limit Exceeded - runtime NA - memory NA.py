class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        vel=(nums,k)
        subarr_val=[]
        for i in range(n):
            minval=nums[i]
            maxval=nums[i]
            for j in range(i,n):
                minval=min(minval,nums[j])
                maxval=max(maxval,nums[j])
                val=maxval-minval
                subarr_val.append(val)
        return sum(heapq.nlargest(k,subarr_val))