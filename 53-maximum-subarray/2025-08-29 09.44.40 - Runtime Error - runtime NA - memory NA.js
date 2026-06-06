/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let maxi=Number.MIN_VALUE,n=nums.length,sum=0;
       for(let i=0;i<n;i++){
        let cur=nums[i];
        sum=Math.max(cur,sum+cur);
        maxi=Math.max(maxi,sum);
       }
       return maxi; 
};