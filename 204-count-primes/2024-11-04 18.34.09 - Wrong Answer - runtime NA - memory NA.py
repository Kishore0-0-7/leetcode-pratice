class Solution(object):
    def countPrimes(self, n):
        count=1
        if n<=2:
            return 0
        for i in range(2,n):
            for j in range(2,int(i**0.5)+1):
                if(i%j==0):
                    continue
                else:
                    count+=1
        return count
                
        

        