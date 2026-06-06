class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        d={}
        a=sorted(nums)
        for i,num in enumerate (a):
            if num not in d:
                d[num]=i
        r=[]
        for i in nums:
            r.append(d[i])
        return r