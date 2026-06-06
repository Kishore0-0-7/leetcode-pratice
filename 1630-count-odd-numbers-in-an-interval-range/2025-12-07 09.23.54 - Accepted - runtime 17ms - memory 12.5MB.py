class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        lst=[]
        if low&1==0:
            low+=1
        if high&1==0:
            high-=1
        return (high-low)/2+1