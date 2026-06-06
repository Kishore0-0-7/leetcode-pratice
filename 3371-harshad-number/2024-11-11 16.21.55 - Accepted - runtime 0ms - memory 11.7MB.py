class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        n=sum(int (i) for i in str (x))
        return n if x%n==0 else -1