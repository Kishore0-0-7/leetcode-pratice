int minimumArea(int** grid, int gridSize, int* gridColSize) {
        int minrow=gridSize;
        int maxrow=-1;
        int mincol=gridColSize[0];
        int maxcol=-1;
        for(int i=0;i<gridSize;i++){
            for(int j=0;j<gridColSize[0];j++){
                if(grid[i][j]==1){
                    minrow=minrow>i?i:minrow;
                    maxrow=maxrow>i?maxrow:i;
                    mincol=mincol>j?j:mincol;
                    maxcol=maxcol>j?maxcol:j;
                }
            }
        }
        return (maxrow-minrow+1)*(maxcol-mincol+1);
}