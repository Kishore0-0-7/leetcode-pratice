class Solution {
    public int maxSumRangeQuery(int[] nums, int[][] requests) {
        int n = nums.length;
        Arrays.sort(nums);
        long mod = 1000000007L;

        long[] freq = new long[n + 1];
        for (int[] req : requests) {
            int l = req[0], r = req[1];
            freq[l] += 1;
            if (r + 1 < n) freq[r + 1] -= 1;
        }

        for (int i = 1; i < n; i++) {
            freq[i] += freq[i - 1];
        }

        long[] weights = new long[n];
        for (int i = 0; i < n; i++) {
            weights[i] = freq[i];
        }

        Arrays.sort(weights);

        long res = 0;
        for (int i = 0; i < n; i++) {
            res = (res + nums[i] * weights[i]) % mod;
        }
        return (int) res;
    }
}