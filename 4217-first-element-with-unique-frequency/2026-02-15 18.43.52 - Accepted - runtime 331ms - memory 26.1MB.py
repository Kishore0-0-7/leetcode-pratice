class Solution(object):
    def firstUniqueFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        fd={}
        for v in d.values():
            fd[v]=fd.get(v,0)+1
        for i in nums:
            if fd[d[i]]==1:
                return i
        return -1