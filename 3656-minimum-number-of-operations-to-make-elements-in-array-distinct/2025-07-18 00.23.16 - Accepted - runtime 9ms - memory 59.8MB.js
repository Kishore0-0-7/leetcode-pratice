/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function(nums) {
     let count = 0;
        while (nums.length > new Set(nums).size) {
            nums = nums.slice(3);
            count++;
        }
        return count;
};