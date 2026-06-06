class Solution {
public:
    int smallestRepunitDivByK(int k) {
        if (k % 10 != 1 && k % 10 != 3 && k % 10 != 7 && k % 10 != 9) return -1;

        int mod = 0;
        unordered_set<int> modSet;

        for (int length = 1; length <= k; ++length) {
            mod = (10 * mod + 1) % k;
            if (mod == 0) return length;
            if (modSet.count(mod)) return -1;
            modSet.insert(mod);
        }

        return -1;
    }
};