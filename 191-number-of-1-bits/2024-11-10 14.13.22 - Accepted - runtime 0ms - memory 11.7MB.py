class Solution(object):
    def hammingWeight(self, n):
        a=0
        while(n>0):
            a+=n&1
            n=n>>1;
        return a
