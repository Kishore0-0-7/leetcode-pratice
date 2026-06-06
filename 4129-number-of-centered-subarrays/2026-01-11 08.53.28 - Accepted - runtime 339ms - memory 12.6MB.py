class Solution(object):
    def centeredSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ans=0
        for i in range(n):
            curr_sum=0
            seen=set()
            for j in range(i, n):
                curr_sum+=nums[j]
                seen.add(nums[j])
                if curr_sum in seen:
                    ans+=1
        return ans