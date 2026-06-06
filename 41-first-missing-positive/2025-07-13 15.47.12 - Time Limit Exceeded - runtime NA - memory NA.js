/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    let i=1;
    const unique = [...new Set(nums)];
    while(unique.includes(i))
    i++;
    return i;
};