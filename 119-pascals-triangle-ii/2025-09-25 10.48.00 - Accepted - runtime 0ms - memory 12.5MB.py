class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        lst=[]
        for i in range(rowIndex+1):
            r=[1]*(i+1)
            for j in range(1,i):
                r[j]=lst[i-1][j-1]+lst[i-1][j]
            lst.append(r)
        return lst[rowIndex]