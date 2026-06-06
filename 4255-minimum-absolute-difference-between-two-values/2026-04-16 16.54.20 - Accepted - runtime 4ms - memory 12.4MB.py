class Solution(object):
    def minAbsoluteDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=-1
        j=-1
        ans=float('inf')
        for k in range(len(nums)):
            if nums[k]==1:
                i=k
                if(i!=-1 and j!=-1):
                    ans=min(ans,(abs(i-j)))
            if nums[k]==2:
                j=k
                if(i!=-1 and j!=-1):
                    ans=min(ans,abs(i-j))
        return ans if ans!=float('inf') else -1