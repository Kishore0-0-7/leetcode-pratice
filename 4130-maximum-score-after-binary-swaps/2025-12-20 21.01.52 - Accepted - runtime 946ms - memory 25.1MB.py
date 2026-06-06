class Solution(object):
    def maximumScore(self, nums, s):
        """
        :type nums: List[int]
        :type s: str
        :rtype: int
        """
        mh=[]
        b=0
        sc=0
        for i in range(len(nums)):
            heapq.heappush(mh,-nums[i])
            if s[i]=="1":
              sc+= -heapq.heappop(mh)
        return sc