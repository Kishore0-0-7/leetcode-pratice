class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        n=sum(int(i) for i in str(x))
        if x%n==0:
            return n
        else:
            return -1