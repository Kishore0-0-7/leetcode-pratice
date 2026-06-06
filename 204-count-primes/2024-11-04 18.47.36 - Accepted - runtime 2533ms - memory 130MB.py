class Solution(object):
    def countPrimes(self, n):
        if n<=2:
            return 0
        p=[True]*n
        p[0]=p[1]=False
        for i in range(2,(int(n**0.5)+1)):
            if p[i]:
                for j in range(i*i,n,i):
                    p[j]=False

        return sum(p)      
        

        