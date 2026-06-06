/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums) {
    let mx=0;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > nums[mx]) {
            mx = i;
        }
    }
    return mx;
};