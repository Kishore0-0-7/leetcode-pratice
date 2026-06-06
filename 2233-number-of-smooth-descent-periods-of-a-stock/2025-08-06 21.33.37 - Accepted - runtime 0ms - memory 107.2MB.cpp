class Solution {
public:
    long long getDescentPeriods(vector<int>& prices) {
      int l = 0;
        long long ans = 0;
        int n = prices.size();
        for (int r = 0; r < n; r++) {
            if (r > 0 && prices[r] != prices[r - 1] - 1) {
                l = r;
            }
            ans += (r - l + 1);
        }
        return ans;  
    }
};