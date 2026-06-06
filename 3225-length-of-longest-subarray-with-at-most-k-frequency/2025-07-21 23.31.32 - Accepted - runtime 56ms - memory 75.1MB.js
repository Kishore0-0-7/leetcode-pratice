/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxSubarrayLength = function(nums, k) {
    const count = new Map();
    let res = 0, i = 0, n = nums.length;

    for (let j = 0; j < n; ++j) {
      count.set(nums[j], (count.get(nums[j]) || 0) + 1);

      while (count.get(nums[j]) > k) {
        count.set(nums[i], count.get(nums[i]) - 1);
        i++;
      }

      res = Math.max(res, j - i + 1);
    }

    return res;
};