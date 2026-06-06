class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int ones = 0;
        for (int i=0; i<s.length();i++) {
            if (s[i]=='1') {
                s[i]='0';
                ones++;
            }
        }
        if (ones>1) {
            for (int i=0;i<ones-1;i++) {
                s[i]='1';
            }
        }
        s[s.length()-1]='1';
        return s;
    }
};