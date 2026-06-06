class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        lst=[]
        for i in bulbs:
            if i in lst:
                lst.remove(i)
            else:
                lst.append(i)
        return sorted(lst)