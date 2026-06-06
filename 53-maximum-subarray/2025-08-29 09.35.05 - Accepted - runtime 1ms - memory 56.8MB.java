class Solution {
    public int maxSubArray(int[] nums) {
       int max=Integer.MIN_VALUE,n=nums.length,sum=0;
       for(int i=0;i<n;i++){
        int cur=nums[i];
        sum=Math.max(cur,sum+cur);
        max=Math.max(max,sum);
       }
       return max; 
    }
}