class Solution(object):
    def isPowerOfTwo(self, n):
        num=0
        while n>pow(2,num):
            num+=1
        return n==pow(2,num)