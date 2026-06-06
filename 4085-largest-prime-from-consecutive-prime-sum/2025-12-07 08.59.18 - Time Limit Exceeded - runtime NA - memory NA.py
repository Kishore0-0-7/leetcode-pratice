class Solution(object):
    def largestPrime(self, n):
        """
        :type n: int
        :rtype: int
        """    
        lst=[2]
        for i in range(3,n/2+2):
            if self.findPrime(i):
                lst.append(i)
        t,a=0,0
        for p in lst:
            t+=p
            if t>n:
                break
            if self.findPrime(t):
                a=t
        return a
    def findPrime(self,n):
        if n<2: return False
        if n%2==0 and n!=2: return False
        x=int(n**0.5)
        for i in range(3,x+1,2):
            if n%i==0: return False
        return True