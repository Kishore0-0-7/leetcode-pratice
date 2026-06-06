public class Solution {
    public int MakeTheIntegerZero(int num1, int num2) {
        for (int k = 1; k <= 60; k++) {
            long x = (long)num1 - (long)num2 * k;

            if (x < k) {
                return -1;
            }

            if (k >= BitOperations.PopCount((ulong)x)) {
                return k;
            }
        }
        return -1;
    }
}