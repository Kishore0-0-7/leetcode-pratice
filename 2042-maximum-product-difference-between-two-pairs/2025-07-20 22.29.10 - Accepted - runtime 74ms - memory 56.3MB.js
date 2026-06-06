/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProductDifference = function(nums) {
        nums.sort((a,b) => a - b)
        let n=nums.length;
        
        let p1=nums[n-2]*nums[n-1];
        let p2=nums[0]*nums[1];
        
        let res=p1-p2;
        
        return res;
};