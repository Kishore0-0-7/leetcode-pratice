class Solution {
    public int areaOfMaxDiagonal(int[][] dimensions) {
        double maxd=0;
        int maxa=0;
        for(int []lst : dimensions){
            double curd=Math.sqrt(lst[0]*lst[0]+lst[1]*lst[1]);
            int cura=lst[0]*lst[1];
            if((curd>maxd)||(curd==maxd && maxa<cura)){
                maxd=curd;
                maxa=cura;
            }
        }
        return maxa;
    }
}