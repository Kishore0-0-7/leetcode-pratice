class Solution(object):
    def transpose(self, matrix):
        l=[]
        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            l.append(temp)
        return l
        