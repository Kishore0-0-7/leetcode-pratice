/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var maxUncrossedLines = function(nums1, nums2) {
    let m = nums1.length, n = nums2.length;
    
    if (m < n) {
        [nums1, nums2] = [nums2, nums1];
        [m, n] = [n, m];
    }

    let dp = new Array(n + 1).fill(0);

    for (let i = 1; i <= m; i++) {
        let prev = 0;
        for (let j = 1; j <= n; j++) {
            let curr = dp[j];
            if (nums1[i - 1] === nums2[j - 1]) {
                dp[j] = prev + 1;
            } else {
                dp[j] = Math.max(dp[j - 1], curr);
            }
            prev = curr;
        }
    }
    return dp[n];
};