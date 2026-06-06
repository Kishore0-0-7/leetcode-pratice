  class Solution {
    public int dominantIndices(int[] nums) {
        int n = nums.length;
        if (n < 2) return 0;
        int tSum = 0;
        for (int x : nums) tSum += x;
        int sum = 0;
        int pSum = 0;
        for (int i = 0; i < n - 1; i++) {
            pSum += nums[i];
            int sR = tSum - pSum;
            int cR = n - i - 1;
            if ((long) nums[i] * cR > sR) {
                sum++;
            }
        }
        return sum;
    }
}
