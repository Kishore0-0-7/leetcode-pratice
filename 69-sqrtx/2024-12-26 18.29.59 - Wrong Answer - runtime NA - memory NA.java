class Solution {
    public int mySqrt(int x) {
       int c=0;
       while(((c+1)*(c+1))<=x){
        c+=1;
       } 
       return c;
    }
}