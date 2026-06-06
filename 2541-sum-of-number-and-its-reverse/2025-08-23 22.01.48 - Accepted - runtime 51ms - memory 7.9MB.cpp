class Solution {
public:
    bool sumOfNumberAndReverse(int num) {
        for (int i = 0; i <= num; i++) {
            int rev = reverseNum(i);
            if (i + rev == num) return true;
        }
        return false;
    }

private:
    int reverseNum(int n) {
        int rev = 0;
        while (n > 0) {
            rev = rev * 10 + (n % 10);
            n /= 10;
        }
        return rev;
    }
};