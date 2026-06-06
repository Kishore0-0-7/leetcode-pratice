class Solution(object):
    def fact(self,n):
        if n<=1:
            return 1
        return n*self.fact(n-1)
    def trailingZeroes(self, n):
        if n<=0:
            return 0
        count=0
        num=self.fact(n)
        while(num > 0 and num%10==0):
            count+=1
            num//=10
        return count