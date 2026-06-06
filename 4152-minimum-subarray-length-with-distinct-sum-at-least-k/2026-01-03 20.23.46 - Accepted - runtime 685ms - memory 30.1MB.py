class Solution(object):
    def minLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq=defaultdict(int)
        ds=0
        l=0
        ans=float('inf')
        for r in range(len(nums)):
            if freq[nums[r]]==0:
                ds+=nums[r]
            freq[nums[r]]+=1
            while ds>=k:
                ans=min(ans,r-l+1)
                freq[nums[l]]-=1
                if freq[nums[l]]==0:
                    ds-=nums[l]
                l+=1
        return ans if ans!=float('inf') else -1