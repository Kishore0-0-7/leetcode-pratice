class Solution(object):
    def arrangeCoins(self, n):
        i=0
        while i<=n:
            n-=i
            i+=1
        return i-1
        