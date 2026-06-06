class Solution(object):
    def modifiedMatrix(self, matrix):
        result = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
        for i in range(len(result)):
            for j in range(len(result[0])):
                if result[i][j]==-1:
                    result[i][j]=max(result[i])
        matrix = [[result[j][i] for j in range(len(result))] for i in range(len(result[0]))]
        return matrix