/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var maximumScore = function(a, b, c) {
    return Math.min(Math.floor((a + b + c) / 2), a + b + c - Math.max(a, b, c));
};