class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        hmap={}
        mini=float('inf')
        for idx,val in enumerate(list1):
            hmap[val]=idx
        for idx,val in enumerate(list2):
            if val in hmap:
                total=idx+hmap.get(val)
                if total<mini:
                    mini=total
                    res=[val]
                elif total==mini:
                    res.append(val)
        return res