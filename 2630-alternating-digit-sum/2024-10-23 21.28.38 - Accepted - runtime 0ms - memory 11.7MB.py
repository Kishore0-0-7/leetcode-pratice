class Solution(object):
    def alternateDigitSum(self, n):
        st=0
        for i in range(len(str(n))):
            st += -int(str(n)[i]) if i % 2 != 0 else int(str(n)[i])
        return st
            

        