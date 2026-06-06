class Solution(object):
    def countPrimes(self, n):
        count=1
        lst=[]
        m=0
        for i in range(2,n+1):
            for j in range(2,(i/2)+1):
                if(i%j==0):
                    count+=1
                    break

        return(n if n<=0 else n-count)
        

        