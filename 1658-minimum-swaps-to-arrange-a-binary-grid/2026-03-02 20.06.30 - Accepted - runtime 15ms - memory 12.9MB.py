class Solution(object):
    def minSwaps(self,grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        trailing_zeros=[]
        for row in grid:
            count=0
            for val in reversed(row):
                if val==0:
                    count+=1
                else:
                    break
            trailing_zeros.append(count)
        swaps=0
        for i in range(n):
            needed=n-i-1
            j=i
            while j<n and trailing_zeros[j]<needed:
                j+=1
            if j==n:
                return -1
            while j > i:
                trailing_zeros[j],trailing_zeros[j-1]=trailing_zeros[j-1],trailing_zeros[j]
                swaps+=1
                j-=1
        return swaps