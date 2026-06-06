class Solution(object):
    def isSameAfterReversals(self, num):
        a=int(str(num)[::-1])
        return num==int(str(a)[::-1])