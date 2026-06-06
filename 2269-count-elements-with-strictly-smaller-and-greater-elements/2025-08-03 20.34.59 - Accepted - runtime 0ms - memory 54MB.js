/**
 * @param {number[]} nums
 * @return {number}
 */
var countElements = function(nums) {
    const max = Math.max(...nums);
    const min = Math.min(...nums);
    let count = 0;

    nums.forEach(num => {
        if (num < max && num > min) count++
    })
    return count;
};