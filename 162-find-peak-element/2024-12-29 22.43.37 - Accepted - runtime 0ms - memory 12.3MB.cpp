class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int mx = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > nums[mx]) {
                mx = i;
            }
        }
        return mx;
    }
};