class Solution {
public:
    int countOfSubstrings(string s, int k) {
        int ans = 0;
    int n = s.length();

    for (int i = 0; i < n; i++) {
        int a = 0, e = 0, i_count = 0, o = 0, u = 0, c = 0;

        for (int j = i; j < n; j++) {
            char ch = s[j];
            if (ch == 'a') a++;
            else if (ch == 'e') e++;
            else if (ch == 'i') i_count++;
            else if (ch == 'o') o++;
            else if (ch == 'u') u++;
            else c++;

            if (a > 0 && e > 0 && i_count > 0 && o > 0 && u > 0 && c == k) {
                ans++;
            }
        }
    }

    return ans;
    }
};