class Solution(object):
    def alternateDigitSum(self, n):
        num=0
        st=str(n)
        for i in range(len(st)):
            num = num+int(st[i]) if i%2==0 else num-int(st[i])
        return num
            

        