/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let min=nums[0];
        for(let i=1;i<nums.length;i++)
        min=Math.min(min,nums[i]);
        return min;
};