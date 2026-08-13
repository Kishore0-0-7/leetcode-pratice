class Solution {
    public int minSwapsCouples(int[] row) {
     int cnt=0,n=row.length;
     for(int i=0;i<n;i+=2){
        int partner=row[i]^1;
        if(partner==row[i+1]) continue;
        for(int j=i+2;j<n;j++){
            if(row[j]==partner){
                swap(row,i+1,j);
                cnt++;
                break;
            }
        }
     }
        return cnt;
     }
     private static void swap(int[] row,int i,int j){
        int t=row[i];
        row[i]=row[j];
        row[j]=t;
     }
}