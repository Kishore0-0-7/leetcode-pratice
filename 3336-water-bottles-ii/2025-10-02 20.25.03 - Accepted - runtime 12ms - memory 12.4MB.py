class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        ans=numBottles
        while numBottles>=numExchange:
            numBottles-=numExchange-1
            numExchange+=1
            ans+=1
        return ans