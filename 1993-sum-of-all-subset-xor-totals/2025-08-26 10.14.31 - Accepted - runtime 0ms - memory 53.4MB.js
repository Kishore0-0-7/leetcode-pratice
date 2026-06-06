/**
 * @param {number[]} nums
 * @return {number}
 */
var subsetXORSum = function(nums) {
    let total=0;
    for (let num of nums)
        total |=num;
    return total*(1<<(nums.length-1));
};