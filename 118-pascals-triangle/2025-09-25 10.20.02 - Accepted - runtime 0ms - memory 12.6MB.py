class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        lst=[]
        for i in range(numRows):
            r=[1]*(i+1)
            for j in range(1,i):
                r[j]=lst[i-1][j-1]+lst[i-1][j]
            lst.append(r)
        return lst
