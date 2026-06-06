/**
 * @param {number[]} nums
 * @return {number}
 */
var triangularSum = function(nums) {
    let n=nums.length;
    
        for (let size=n;size>1;size--) {
            for (let i=0;i<size-1;i++) {
                nums[i]=(nums[i]+nums[i+1])%10;
            }
        }
        return nums[0];
};