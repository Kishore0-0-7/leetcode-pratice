class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        int n = code.size();
        vector<int> result(n, 0);

        for (int i = 0; i < n; ++i) {
            int total = 0;
            if (k > 0) {
                for (int j = 1; j <= k; ++j) {
                    total += code[(i + j) % n];
                }
            } else if (k < 0) {
                for (int j = 1; j <= -k; ++j) {
                    total += code[(i - j + n) % n];
                }
            }
            result[i] = total;
        }

        return result;
    }
};