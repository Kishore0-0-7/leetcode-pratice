class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(key=abs,reverse=True)
        n=len(nums)
        m=(n+1)//2
        ps=sum(x*x for x in nums[:m])
        ns=sum(x*x for x in nums[m:])
        return ps-ns