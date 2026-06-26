class Solution {
    public int[] cycleLengthQueries(int n, int[][] queries) {
        int l=queries.length;
        int num[]=new int[l];
        int q1,q2,c;
        for(int i=0;i<l;i++){
            q1=queries[i][0];
            q2=queries[i][1];
            c=0;
            while(q1!=q2){
                if(q1>q2) q1/=2;
                else q2/=2;
                c++;
            }
            num[i]=c+1;
        }
        return num;
    }
}