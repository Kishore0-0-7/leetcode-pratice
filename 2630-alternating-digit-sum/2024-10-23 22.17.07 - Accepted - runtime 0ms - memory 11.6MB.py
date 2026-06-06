class Solution(object):
    def alternateDigitSum(self, n):
        st=0
        for i in range(len(str(n))):
            if i%2==0:
                st=st+int(str(n)[i])  
            else:
                st+=-int(str(n)[i])
        return st
            

        