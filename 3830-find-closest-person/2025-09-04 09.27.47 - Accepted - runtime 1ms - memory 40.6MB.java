class Solution {
    public int findClosest(int x, int y, int z) {
        int l1=Math.abs(x-z);
        int l2=Math.abs(y-z);
        if(l1>l2)
            return 2;
        else if(l1<l2)
            return 1;
        return 0;
    }
}