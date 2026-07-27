class Solution {
    int dx[]={-1,1,0,0};
    int dy[]={0,0,-1,1};
    void dfs(int[][] image,int row,int col,int og,int color){
        if(row<0||col<0||
        row>=image.length||col>=image[0].length) return;
        if(image[row][col]!=og) return;
        image[row][col]=color;
        for(int i=0;i<4;i++){
            int nr=row+dx[i];
            int nc=col+dy[i];
            dfs(image,nr,nc,og,color);
        }
    }
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int og=image[sr][sc];
        if(og==color) return image;
        dfs(image,sr,sc,og,color);
        return image;
    }

}