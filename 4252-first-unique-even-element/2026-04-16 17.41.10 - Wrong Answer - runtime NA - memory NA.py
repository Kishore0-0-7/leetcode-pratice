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
        for k,v in dd.items():
            if v==1:
                return k
        return -1