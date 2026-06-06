class Solution(object):
    def firstUniqueEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        dd=defaultdict(int)
        for n in nums:
            if n%2==0:
                dd[n]+=1
        for n in nums:
            if n%2==0 and dd[n]==1:
                return n
        return -1