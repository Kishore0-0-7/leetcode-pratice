class Solution {
    public int numberOfGoodSubarraySplits(int[] nums) {
      long cnt = 0;
        int lo = -1;
        long MOD = 1000000007;

        for (int hi = 0; hi < nums.length; hi++) {
            if (nums[hi] == 1) {
                if (cnt == 0) {
                    cnt = 1;
                } else {
                    cnt = (cnt * (hi - lo)) % MOD;
                }
                lo = hi;
            }
        }
        return (int) cnt;  
    }
}