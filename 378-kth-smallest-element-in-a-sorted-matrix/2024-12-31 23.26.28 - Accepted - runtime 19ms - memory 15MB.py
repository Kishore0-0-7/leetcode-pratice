class Solution(object):
    def kthSmallest(self, matrix, k):
        lst=[]
        n=len(matrix)
        for i in range (n):
            for j in range (n):
                lst.append(matrix[i][j])

        lst.sort()
        return lst[k-1]
        