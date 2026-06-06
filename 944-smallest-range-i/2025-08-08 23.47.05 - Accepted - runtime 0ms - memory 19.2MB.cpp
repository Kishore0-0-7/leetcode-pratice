class Solution {
public:
    int smallestRangeI(vector<int>& nums, int k) {
        int min_val = nums[0], max_val = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            min_val = min(min_val, nums[i]);
            max_val = max(max_val, nums[i]);
        }
        int diff = max_val - min_val;
        int reduced = diff - 2 * k;
        return max(0, reduced);
    }
};