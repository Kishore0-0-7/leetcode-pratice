/**
 * @param {number} k
 * @return {number}
 */
var minOperations = function(k) {
    let v = Math.floor(Math.sqrt(k));
    return v + Math.floor((k - 1) / v) - 1
};