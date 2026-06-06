 class Solution {
    public int longestAlternating(int[] nums) {
        int n = nums.length;
        if (n == 1) return 1;

        int[] keep = new int[n]; // no deletion used
        int[] drop = new int[n]; // one deletion used

        keep[0] = 1;
        keep[1] = nums[1] != nums[0] ? 2 : 1;

        drop[0] = 1;
        drop[1] = 2; // delete either nums[0] or nums[1]

        int ans = Math.max(keep[1], drop[1]);

        for (int i = 2; i < n; i++) {
            int d1 = nums[i] - nums[i - 1];
            int d2 = nums[i - 1] - nums[i - 2];

            // keep[i]: no deletion
            if (d1 != 0 && d2 != 0 && d1 * d2 < 0) {
                keep[i] = keep[i - 1] + 1;
            } else if (d1 != 0) {
                keep[i] = 2;
            } else {
                keep[i] = 1;
            }

            // drop[i]: one deletion allowed
            // Option 1: delete nums[i]
            drop[i] = keep[i - 1];

            // Option 2: delete nums[i-1]
            int d3 = nums[i] - nums[i - 2];
            if (d3 != 0 && d2 != 0 && d3 * d2 < 0) {
                drop[i] = Math.max(drop[i], keep[i - 2] + 1);
            }

            // Option 3: already deleted earlier
            if (d1 != 0 && d2 != 0 && d1 * d2 < 0) {
                drop[i] = Math.max(drop[i], drop[i - 1] + 1);
            }

            ans = Math.max(ans, Math.max(keep[i], drop[i]));
        }

        return ans;
    }
}
