class Solution(object):
    def countPrimes(self, n):
        count=1
        if n<=2:
            return 0
        for i in range(3,n,2):
            p=True
            for j in range(3,int(i**0.5)+1,2):
                if(i%j==0):
                    p=False
                    break
            if(p==True):
                count+=1
        return count