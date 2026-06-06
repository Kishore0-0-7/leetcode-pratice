class Solution(object):
    def sumOfUnique(self, nums):
        a={}
        for i in nums:
            a[i] = a.get(i, 0) + 1
        sum=0
        for k,v in a.items():
            if v==1 : sum+=k
        return sum