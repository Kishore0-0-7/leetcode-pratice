int maxSubArray(int* nums, int numsSize) {
    int maxi=INT_MIN,n=numsSize,sum=0;
       for(int i=0;i<n;i++){
        int cur=nums[i];
        sum=cur>(sum+cur)?cur:sum+cur;
        maxi=maxi>sum?maxi:sum;
       }
       return maxi;
}