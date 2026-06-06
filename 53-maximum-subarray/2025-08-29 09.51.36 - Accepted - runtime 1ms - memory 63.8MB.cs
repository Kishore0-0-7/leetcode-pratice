public class Solution {
    public int MaxSubArray(int[] nums) {
       int maxi=int.MinValue,n=nums.Length,sum=0;
       for(int i=0;i<n;i++){
        int cur=nums[i];
        sum=cur>(sum+cur)?cur:sum+cur;
        maxi=maxi>sum?maxi:sum;
       }
       return maxi; 
    }
}