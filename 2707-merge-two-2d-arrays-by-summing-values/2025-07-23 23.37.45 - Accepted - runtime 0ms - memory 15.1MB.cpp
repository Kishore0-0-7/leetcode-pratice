class Solution {
public:
    vector<vector<int>> mergeArrays(vector<vector<int>>& nums1, vector<vector<int>>& nums2) {
        map<int, int> m;
        for (auto& p : nums1) m[p[0]] += p[1];
        for (auto& p : nums2) m[p[0]] += p[1];
        
        vector<vector<int>> res;
        for (auto& [k, v] : m) {
            res.push_back({k, v});
        }
        
        return res;
    }
};