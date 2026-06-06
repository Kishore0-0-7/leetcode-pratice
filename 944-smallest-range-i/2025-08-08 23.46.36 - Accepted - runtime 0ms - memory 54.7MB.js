/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var smallestRangeI = function(nums, k) {
    let min = Math.min(...nums);
    let max = Math.max(...nums);
    let diff = max - min;
    let reduced = diff - 2 * k;
    return Math.max(0, reduced);
};