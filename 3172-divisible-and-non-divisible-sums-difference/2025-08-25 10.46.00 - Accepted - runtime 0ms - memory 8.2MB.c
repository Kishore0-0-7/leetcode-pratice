int differenceOfSums(int n, int m) {
    int div=0,nondiv=0;
        for(int i=1;i<n+1;i++)
            i%m==0?(div+=i):(nondiv+=i);
        return nondiv-div;
}