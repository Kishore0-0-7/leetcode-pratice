class Solution {
    public int smallestNumber(int n) {
        for (int i=0;(n&(n+1))!=0;i++) {
            n|=1<<i;
        }
        return n;
    }
}