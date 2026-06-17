class Solution {
    public int maxSubArray(int[] nums) {
        int mx=Integer.MIN_VALUE;
        int sum=0;
        for(int n:nums){
            sum+=n;
            mx=(mx>sum)?mx:sum;
            sum=(sum<0)?0:sum;
        }
        return mx;
    }
}