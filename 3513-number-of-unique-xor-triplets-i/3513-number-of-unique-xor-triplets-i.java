class Solution {
    public int uniqueXorTriplets(int[] nums) {
        int n=nums.length;
        if(n<=2) return n;
        int x=1,c=-1;
        while(x<=n){
            x<<=1;
            c++;
        }
        return 1<<(c+1);
    }
}