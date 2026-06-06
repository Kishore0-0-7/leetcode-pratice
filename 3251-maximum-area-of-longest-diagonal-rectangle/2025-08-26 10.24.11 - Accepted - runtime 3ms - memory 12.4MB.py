class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        maxd=0
        maxa=0
        for lst in dimensions:
            curd=sqrt(lst[0]*lst[0]+lst[1]*lst[1])
            cura=lst[0]*lst[1]
            if curd>maxd or(curd==maxd and maxa<cura):
                maxd=curd
                maxa=cura
        return maxa
