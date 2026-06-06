class Solution {
public:
    int arrangeCoins(int n) {
        int i=0;
        while (i<=n){
            n-=i;
            i+=1;}
        return i-1;
    }
};