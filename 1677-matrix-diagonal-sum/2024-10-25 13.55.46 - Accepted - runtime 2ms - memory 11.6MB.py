class Solution(object):
    def diagonalSum(self, mat):
        n=len(mat)
        sum=0
        for  i in range(n):
                sum=sum+mat[i][i]+mat[i][n-i-1]
        if(n%2!=0):
            sum=sum-mat[(n-1)/2][(n-1)/2]
        return sum