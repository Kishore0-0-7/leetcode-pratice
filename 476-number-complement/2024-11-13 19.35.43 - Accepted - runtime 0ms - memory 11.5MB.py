class Solution(object):
    def findComplement(self, num):
        n=str(bin(num))[2:]
        n1=''
        for i in n:
            if i=='1':
                n1+='0'
            else:
                n1+='1'  
        return int(n1,2)