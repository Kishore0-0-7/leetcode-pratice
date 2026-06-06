class Solution(object):
    def getSum(self, a, b):
        carry=0
        mask=0xffffffff
        while b&mask!=0:
            carry=a&b
            a=a^b
            b=carry<<1
        return a&mask if b>mask else a
        