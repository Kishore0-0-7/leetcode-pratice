public class Solution {
    public int FindClosest(int x, int y, int z) {
        int l1=Math.Abs(x-z);
        int l2=Math.Abs(y-z);
        if(l1>l2)
            return 2;
        else if(l1<l2)
            return 1;
        return 0;
    }
}