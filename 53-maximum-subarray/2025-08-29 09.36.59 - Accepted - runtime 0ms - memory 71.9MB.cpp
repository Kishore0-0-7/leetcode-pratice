class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxi=INT_MIN,n=nums.size(),sum=0;
       for(int i=0;i<n;i++){
        int cur=nums[i];
        sum=max(cur,sum+cur);
        maxi=max(maxi,sum);
       }
       return maxi;
    }
};