class Solution {
    public int mySqrt(int x) {
       if(x==0)
       return 0;
       int l=1,h=x,mid=0;
       while(l<=h){
        mid=l+(h-l)/2;
        if (mid*mid == x) 
            return mid;
        else if(mid*mid<x)
        l=mid+1;
        else
        h=mid-1;
       }
       return h;  
    }
}