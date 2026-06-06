class Solution {
public:
    vector<int> minSubsequence(vector<int>& nums) {
        sort(nums.rbegin(), nums.rend());
        int total = 0;
        for (int num : nums) total += num;

        int rSum = 0;
        vector<int> res;

        for (int num : nums) {
            rSum += num;
            res.push_back(num);
            if (rSum > total - rSum) break;
        }

        return res;
    }
};