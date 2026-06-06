class Solution {
public:
    int numberOfGoodSubarraySplits(vector<int>& nums) {
     long long cnt = 0;
        int lo = -1;
        const long long MOD = 1000000007;

        for (int hi = 0; hi < nums.size(); hi++) {
            if (nums[hi] == 1) {
                if (cnt == 0) {
                    cnt = 1;
                } else {
                    cnt = (cnt * (hi - lo)) % MOD;
                }
                lo = hi;
            }
        }
        return (int) cnt;   
    }
};