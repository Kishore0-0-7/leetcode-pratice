class Solution(object):
    def getSum(self, a, b):
        while b:
            carry=a&b
            a=a^b
            b=carry<<1
        return a
        