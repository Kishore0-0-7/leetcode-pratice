class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        maxocur=max(dic.values())
        count=0
        for v in dic.values():
            if v==maxocur:
                count+=v
        return count