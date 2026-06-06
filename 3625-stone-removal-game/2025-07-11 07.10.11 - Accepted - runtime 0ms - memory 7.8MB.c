bool canAliceWin(int n) {
    int m=10;
        int t=0;
        while(n>=m){
            n-=m;
            m-=1;
            t=1-t;
        }
        return t!=0;
}