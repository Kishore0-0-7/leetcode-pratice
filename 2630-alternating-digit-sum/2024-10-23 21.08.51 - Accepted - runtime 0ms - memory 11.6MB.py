class Solution(object):
    def alternateDigitSum(self, n):
        n=str(n)
        st=0
        for i in range(len(n)):
            if(i%2!=0):
                st-=int(n[i])
            else:
                st+=int(n[i])
        return st
            

        