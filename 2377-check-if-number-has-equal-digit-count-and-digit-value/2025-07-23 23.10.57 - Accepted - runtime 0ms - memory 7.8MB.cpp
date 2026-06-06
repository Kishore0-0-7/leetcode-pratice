class Solution {
public:
    bool digitCount(string num) {
        for (int i = 0; i < num.size(); i++) {
            int digit = num[i] - '0';
            int count = 0;
            for (int j = 0; j < num.size(); j++) {
                if (num[j] - '0' == i) {
                    count++;
                }
            }
            if (digit != count) {
                return false;
            }
        }
        return true;
    }
};