class Solution {
public:
    int maxSumRangeQuery(vector<int>& nums, vector<vector<int>>& requests) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        const long long mod = 1000000007LL;

        vector<long long> freq(n + 1, 0);
        for (auto &req : requests) {
            int l = req[0], r = req[1];
            freq[l] += 1;
            if (r + 1 < n) freq[r + 1] -= 1;
        }

        for (int i = 1; i < n; i++) {
            freq[i] += freq[i - 1];
        }

        vector<long long> weights(freq.begin(), freq.begin() + n);
        sort(weights.begin(), weights.end());

        long long res = 0;
        for (int i = 0; i < n; i++) {
            res = (res + nums[i] * weights[i]) % mod;
        }
        return (int)res;
    }
};