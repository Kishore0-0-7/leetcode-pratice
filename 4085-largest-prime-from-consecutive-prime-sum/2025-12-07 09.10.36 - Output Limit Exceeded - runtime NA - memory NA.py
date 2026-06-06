class Solution(object):
    def largestPrime(self, n):
        """
        :type n: int
        :rtype: int
        """    
        lst=[True]*(n+1)
        lst[0]=lst[1]=False
        r=int(n**0.5)
        for i in range(2,r+1):
            if lst[i]:
                for j in range(i*i,n+1,i):
                    lst[j]=False
        primes=[i for i in range (2,n+1) if lst[i]==True]
        print(primes)
        t,a=0,0
        for p in primes:
            t+=p
            if t>n:
                break
            if lst[t]:
                a=t
        return a