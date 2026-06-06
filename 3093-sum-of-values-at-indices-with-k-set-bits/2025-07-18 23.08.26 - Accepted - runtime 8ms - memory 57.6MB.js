/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var sumIndicesWithKSetBits = function(nums, k) {
    let total = 0;
        for (let i = 0; i < nums.length; i++) {
            if (i.toString(2).split('1').length - 1 === k) {
                total += nums[i];
            }
        }
        return total;
};