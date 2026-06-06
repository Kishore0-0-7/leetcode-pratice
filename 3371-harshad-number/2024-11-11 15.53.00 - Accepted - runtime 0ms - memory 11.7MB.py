class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        a=str(x)
        n=0
        for i in a:
            n+=int(i)
        if x%n==0:
            return n
        else:
            return -1