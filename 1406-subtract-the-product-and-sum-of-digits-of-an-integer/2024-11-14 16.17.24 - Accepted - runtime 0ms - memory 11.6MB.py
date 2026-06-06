class Solution(object):
    def subtractProductAndSum(self, n):
        num=[i for i in str(n)]
        mul=1
        s=0
        for i in num:
            s+=int(i)
            mul*=int(i)
        return mul-s