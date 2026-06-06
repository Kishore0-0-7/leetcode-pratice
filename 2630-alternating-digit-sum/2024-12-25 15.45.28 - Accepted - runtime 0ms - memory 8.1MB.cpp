class Solution {
public:
    int alternateDigitSum(int n) {
        int m=0;
        while(n>0){
            int d=n%10;
            if((to_string(n).length())%2==1)
            m+=d;
            else
            m-=d;
            n/=10;
        }
        return m;
    }
};