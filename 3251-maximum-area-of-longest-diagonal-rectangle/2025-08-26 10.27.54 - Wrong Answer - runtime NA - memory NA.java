class Solution {
    public int areaOfMaxDiagonal(int[][] dimensions) {
        int maxd=0,maxa=0;
        for(int []lst : dimensions){
            int curd=(int)Math.sqrt(lst[0]*lst[0]+lst[1]*lst[1]);
            int cura=lst[0]*lst[1];
            if((curd>maxd)||(curd==maxd && maxa<cura)){
                maxd=curd;
                maxa=cura;
            }
        }
        return maxa;
    }
}