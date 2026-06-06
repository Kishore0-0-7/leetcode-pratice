class Solution(object):
    def countBits(self, n):
        l=[]
        for i in range(n+1):
            l.append(str(bin(i)).count('1'))
        return l