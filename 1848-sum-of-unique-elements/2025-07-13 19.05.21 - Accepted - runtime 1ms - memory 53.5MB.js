/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfUnique = function(nums) {
    let a={}
    for(let i of nums)
        a[i]=(a[i]||0)+1
    let sum=0
    for(let k in a){
        if (a[k]==1)
        sum+=parseInt(k);
    
    }
    return sum;
};