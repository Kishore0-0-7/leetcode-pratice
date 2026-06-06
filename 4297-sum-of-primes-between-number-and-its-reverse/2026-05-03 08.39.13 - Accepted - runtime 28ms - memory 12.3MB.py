class Solution(object):
    def sumOfPrimesInRange(self, n):
        """
        :type n: int
        :rtype: int
        """
        r=int(str(n)[::-1])
        l=min(n,r)
        h=max(n,r)
        si=[True]*(h+1)
        si[0]=si[1]=False
        for i in range(2,int(h**0.5)+1):
            if si[i]:
                for j in range(i*i,h+1,i):
                    si[j]=False
        a=0
        for i in range(l,h+1):
            if si[i]:
                a+=i
        return a