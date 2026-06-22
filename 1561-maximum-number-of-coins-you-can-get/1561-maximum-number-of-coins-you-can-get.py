class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        r=len(piles)
        count=0
        piles.sort()
        for i in range(r//3):
            count+=piles[r-2]
            r-=2
        return count