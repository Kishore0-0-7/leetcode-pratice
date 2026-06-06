class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n=len(fruits)
        alloted=0
        for i in range(n):
            for j in range(n):
                if fruits[i]<=baskets[j]:
                    baskets[j]=-1
                    alloted+=1
                    break
        return n-alloted
