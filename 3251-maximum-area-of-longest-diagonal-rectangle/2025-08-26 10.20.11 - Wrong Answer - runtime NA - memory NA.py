class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        max=0
        maxlst=[]
        for lst in dimensions:
            cur=sqrt(lst[0]*lst[0]+lst[1]*lst[1])
            if cur>max:
                max=cur
                maxlst=lst
        return maxlst[0]*maxlst[1]
