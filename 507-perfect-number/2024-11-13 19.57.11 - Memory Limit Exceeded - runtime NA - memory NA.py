class Solution(object):
    def checkPerfectNumber(self, num):
        a=[]
        for i in range(1,(num/2)+1):
            if(num%i==0):
                a.append(i)
        return sum(a)==num
        