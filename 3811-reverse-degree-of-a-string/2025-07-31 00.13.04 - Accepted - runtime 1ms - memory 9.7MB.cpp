class Solution {
public:
    int reverseDegree(string s) {
        int ans = 0;
        for (int i = 0; i < s.length(); ++i) {
            int value = s[i] - 'a';
            ans += (i + 1) * (26 - value);
        }
        return ans;
    } 
    
};