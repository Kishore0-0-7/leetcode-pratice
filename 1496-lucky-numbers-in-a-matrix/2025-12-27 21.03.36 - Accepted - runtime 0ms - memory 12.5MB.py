class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n=len(matrix)
        m=len(matrix[0])
        lucky_numbers=[]
        for i in range(n):
            num=float('inf')
            index=-1
            for j in range(m):
                if matrix[i][j]<num:
                    num=matrix[i][j]
                    index=j
            flag=True
            for row in range(n):
                if matrix[row][index]>num:
                    flag=False
                    break
            if flag:
                lucky_numbers.append(num)
        return lucky_numbers