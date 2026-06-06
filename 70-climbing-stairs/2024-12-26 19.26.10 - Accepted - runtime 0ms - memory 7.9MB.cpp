class Solution {
public:
    int climbStairs(int n) {
       if(n<=2)
        return n;
        int x=1,y=2,z=0;
        for (int i=2;i<n;i++){
            z=x+y;
            x=y;
            y=z;
        }
        return z; 
    }
};