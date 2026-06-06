class Solution {
    public int differenceOfSums(int n, int m) {
        int n1=0,n2=0,i;
        for (i=1;i<n+1;i++){
            if(i%m==0)
            n1+=i;
            else
            n2+=i;
        }
        return n2-n1;
    }
}