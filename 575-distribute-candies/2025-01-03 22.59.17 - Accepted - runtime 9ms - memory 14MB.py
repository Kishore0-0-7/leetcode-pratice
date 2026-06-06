class Solution(object):
    def distributeCandies(self, candyType):
        n=len(candyType)//2
        l=len(set(candyType))
        return min(n,l)
        