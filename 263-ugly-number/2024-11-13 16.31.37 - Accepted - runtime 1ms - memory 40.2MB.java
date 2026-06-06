class Solution {
    public boolean isUgly(int n) {
        if (n==0)
        return false;
        int ar[]={2,3,5};
        for (int i=0;i<3;i++){
        while(n%ar[i]==0)
        n/=ar[i];
    }
    return n==1 ;
}
}