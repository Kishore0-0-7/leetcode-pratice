class Solution(object):
    def alternateDigitSum(self, n):
        st=0
        for i in range(len(str(n))):st = st-int(str(n)[i]) if i % 2 != 0 else st+int(str(n)[i])
        return st
            

        