class Solution(object):
    def minDistinctFreqPair(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        for n in nums:
            d[n]=d.get(n,0)+1
        nums.sort()
        x,y=nums[0],-1
        for n in nums:
            z=d[n]
            if z!=d[x]:
                y=n
                break
        return [-1,-1] if y==-1 else [x,y]