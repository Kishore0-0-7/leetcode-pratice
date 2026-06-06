class Solution {
public:
    int getXORSum(vector<int>& arr1, vector<int>& arr2) {
       int ans1 = 0, ans2 = 0;
        for (int num : arr1) {
            ans1 ^= num;
        }
        for (int num : arr2) {
            ans2 ^= num;
        }
        return ans1 & ans2; 
    }
};