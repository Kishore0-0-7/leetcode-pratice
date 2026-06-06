class Solution(object):
    def minArraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx=max(nums)
        pr=set(nums)
        b=[0]*(mx+1)
        for d in sorted(pr):
            for mul in range(d,mx+1,d):
                if b[mul]==0:
                    b[mul]=d
        ans=0
        for x in nums:
            ans+=b[x]
        return ans