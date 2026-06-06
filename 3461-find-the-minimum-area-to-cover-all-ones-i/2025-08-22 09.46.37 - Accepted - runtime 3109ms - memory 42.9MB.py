class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        minrow=len(grid)
        maxrow=-1
        mincol=len(grid[0])
        maxcol=-1
        for i in range (len(grid)):
            for j in range (len(grid[0])):
                if(grid[i][j]==1):
                    minrow=min(minrow,i)
                    maxrow=max(maxrow,i)
                    mincol=min(mincol,j)
                    maxcol=max(maxcol,j)
        return (maxrow-minrow+1)*(maxcol-mincol+1)