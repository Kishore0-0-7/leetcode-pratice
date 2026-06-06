/**
 * @param {number[]} nums
 * @param {number[][]} requests
 * @return {number}
 */
var maxSumRangeQuery = function(nums, requests) {
    const n = nums.length;
    nums.sort((a, b) => a - b);
    const freq = new Array(n + 1).fill(0);
    const mod = 1_000_000_007n;

    for (let [l, r] of requests) {
        freq[l] += 1;
        if (r + 1 < n) freq[r + 1] -= 1;
    }

    for (let i = 1; i < n; i++) {
        freq[i] += freq[i - 1];
    }

    let weights = freq.slice(0, n).sort((a, b) => a - b);

    let res = 0n;
    for (let i = 0; i < n; i++) {
        res = (res + BigInt(nums[i]) * BigInt(weights[i])) % mod;
    }
    return Number(res);
};