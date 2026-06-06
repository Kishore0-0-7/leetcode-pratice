/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfSquares = function(nums) {
    let n = nums.length;
    	let total = 0;
    	for (let i = 1; i <= n; i++) {
    		if(n % i == 0) {
    			let val =  nums[i-1];
    			total += val * val;
    		}
		}
    	return total;
};