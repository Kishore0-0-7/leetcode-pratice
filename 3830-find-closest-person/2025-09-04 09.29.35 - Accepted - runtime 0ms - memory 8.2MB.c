int findClosest(int x, int y, int z) {
    int l1=abs(x-z);
        int l2=abs(y-z);
        if(l1>l2)
            return 2;
        else if(l1<l2)
            return 1;
        return 0;
}