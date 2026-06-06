/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    const seen = new Set(nums);
    let i = 1;
    while (seen.has(i))
    i++;
    return i;
};