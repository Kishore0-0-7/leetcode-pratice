class Solution {
public:
    vector<int> findIntersectionValues(vector<int>& nums1, vector<int>& nums2) {
        vector<int> f1(101, 0);
        vector<int> f2(101, 0);
        for (int i = 0; i < nums1.size(); i++)
            f1[nums1[i]]++;
        for (int i = 0; i < nums2.size(); i++)
            f2[nums2[i]]++;
    
        vector<int> result(2, 0);
        for (int i = 1; i < 101; i++) {
            if (f1[i] && f2[i]) {
                result[0] += f1[i];
                result[1] += f2[i];
            }
        }
        return result;
    }
};