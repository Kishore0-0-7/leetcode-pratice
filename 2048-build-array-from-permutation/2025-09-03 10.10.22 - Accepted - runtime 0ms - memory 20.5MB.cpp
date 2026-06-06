class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        vector<int> temp(nums.size());
        int i=0;
        for(auto n:nums)
        temp[i++]=nums[n];
        return temp;
    }
};