class Solution(object):
    def countElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k==0:
            return len(nums)
        n=len(nums)
        nums.sort()
        kg=nums[n-k]
        c=0
        for x in nums:
            if x<kg:
                c+=1
        return c
        