/**
 * @param {number[]} target
 * @return {number}
 */
var minNumberOperations = function(target) {
    let res = target[0];
        for (let i = 1; i < target.length; ++i)
            res += Math.max(target[i] - target[i - 1], 0);
        return res;  
};