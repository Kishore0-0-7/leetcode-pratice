class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p=[]
        for x in range(1,10001):
            b=bin(x)[2:]
            if b==b[::-1]:
                p.append(x)
        ans=[]
        for x in nums:
            b=float('inf')
            for i in p:
                b=min(b,abs(x-i))
            ans.append(b)
        return ans