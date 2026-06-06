class Solution {
public:
    bool isPalindrome(int x) {
    if (x<0 || x!=0 && x%10==0) return false;
    int c=0;
    while(x>c){
        int d=x%10;
        c=(c*10)+d;
        x/=10;}
        printf("%d",c);
    return (c==x || x==c/10);
    }
};