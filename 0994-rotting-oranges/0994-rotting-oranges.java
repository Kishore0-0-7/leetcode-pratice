class Solution {
    int dx[]={-1,1,0,0};
    int dy[]={0,0,-1,1};
    public int orangesRotting(int[][] grid) {
        int fresh=0,time=0;
        Queue<int []>q=new LinkedList<>();
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j]==1) fresh++;
                else if(grid[i][j]==2){
                q.add(new int[]{i,j});
                }
            }
        }
        while(!q.isEmpty()){
            int s=q.size();
            if(fresh<=0) return time;
            for(int i=0;i<s;i++){
                int[] cur=q.poll();                               
                for(int j=0;j<4;j++){
                    int nr=cur[0]+dx[j];
                    int nc=cur[1]+dy[j];
                    if(nr<0||nc<0||
                    nr>=grid.length||nc>=grid[0].length) continue;
                    if(grid[nr][nc]==1){
                        grid[nr][nc]=2;
                        q.add(new int[]{nr,nc});
                        fresh--;
                    }
                }
            }
            time++;
        }
        return fresh==0?time:-1;
    }
}