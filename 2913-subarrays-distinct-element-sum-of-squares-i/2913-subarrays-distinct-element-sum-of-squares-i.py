class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        result=0
        for i in range(n):
            s=set()
            for j in range(i,n):
                s.add(nums[j])
                result+=len(s)**2
        return result