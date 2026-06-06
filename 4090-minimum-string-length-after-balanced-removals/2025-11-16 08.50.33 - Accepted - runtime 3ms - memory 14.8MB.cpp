class Solution {
public:
    int minLengthAfterRemovals(string s) {
        int a=0,b=0;
        for(char c:s){
            if (c=='a') a+=1;
            else b+=1;
        }
        return a>b?a-b:b-a;
    }
};