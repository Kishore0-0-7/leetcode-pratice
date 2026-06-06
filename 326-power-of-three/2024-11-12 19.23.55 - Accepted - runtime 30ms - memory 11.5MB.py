class Solution(object):
    def isPowerOfThree(self, n):
        i=0
        while(n>pow(3,i)):
            i+=1
        return n==pow(3,i)        