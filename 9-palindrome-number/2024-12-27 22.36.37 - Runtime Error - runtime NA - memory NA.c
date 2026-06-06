bool isPalindrome(int x) {
    if (x<0 || x!=0 && x%10==0) return false;
    int c=0,n=x;
    
    while(n){
        int d=n%10;
        c=(c*10)+d;
        n/=10;}
        printf("%d",c);
    return (c==x);
}