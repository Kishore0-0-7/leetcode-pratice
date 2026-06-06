class Solution(object):
    def hammingWeight(self, n):
       r=0
       while n!=0:
        n=n&(n-1)
        r+=1
       return r
                