class Solution {
    public int alternateDigitSum(int n) {
        String s=Integer.toString(n);
        int m=0;
        while(n>0){
            int d=n%10;
            if((Integer.toString(n)).length()%2==1)
            m+=d;
            else
            m-=d;
            n/=10;
        }
        return m;
    }
}