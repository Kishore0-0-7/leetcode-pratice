class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        f={}
        for i in nums:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        s=0
        for num in f:
            if f[num]%k==0:
                s+=num*f[num]
        return s
                