class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        count_odd = count_even = 0
        for pos in position:
            if(pos%2==0):
                count_even += 1
            else:
                count_odd += 1
        return min(count_odd,count_even)