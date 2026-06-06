class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        e=[]
        s=""
        for i in range(len(nums)):
            s+=str(nums[i])
            d=int(s,2)
            e.append(d%5==0)
        return e