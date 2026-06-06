class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n=nums.size();
        int p1=nums[0]*nums[1];
        int p2=nums[n-1]*nums[n-2];
        int res=p2-p1;
        return res;
    }
};