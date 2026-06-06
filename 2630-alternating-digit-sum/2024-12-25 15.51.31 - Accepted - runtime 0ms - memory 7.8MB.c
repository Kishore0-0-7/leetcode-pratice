int alternateDigitSum(int n) {
    int m=0;
    char st[20];
        while(n>0){
            int d=n%10;
            sprintf(st, "%d", n);
            if(strlen(st)%2==1)
            m+=d;
            else
            m-=d;
            n/=10;
        }
        return m;
    
}