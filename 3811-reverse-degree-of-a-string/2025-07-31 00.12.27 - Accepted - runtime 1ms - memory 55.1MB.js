/**
 * @param {string} s
 * @return {number}
 */
var reverseDegree = function(s) {
    let ans = 0;
    for (let i = 0; i < s.length; i++) {
        let value = s.charCodeAt(i) - 'a'.charCodeAt(0);
        ans += (i + 1) * (26 - value);
    }
    return ans;
};