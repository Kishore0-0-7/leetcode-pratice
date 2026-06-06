class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a={}
        for i in nums:
            if i in a.keys():
                a[i]+=1
            else:
                a[i]=1
        sum=0
        for k,v in a.items():
            if v==1 : sum+=k
        return sum