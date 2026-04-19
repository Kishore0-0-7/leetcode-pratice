class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        px=[0]*n
        sx=[0]*n
        px[0]=nums[0]
        sx[-1]=nums[-1]

        for i in range(1,n):
            px[i]=max(px[i-1],nums[i])

        for i in range(n-2,-1,-1):
            sx[i]=min(sx[i+1],nums[i])

        for i in range(n):
            if px[i]-sx[i]<=k:
                return i
        return -1