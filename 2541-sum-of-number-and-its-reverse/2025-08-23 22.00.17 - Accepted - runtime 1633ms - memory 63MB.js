/**
 * @param {number} num
 * @return {boolean}
 */
var sumOfNumberAndReverse = function(num) {
    function reverse(n) {
        return parseInt(n.toString().split("").reverse().join(""), 10);
    }

    for (let i = 0; i <= num; i++) {
        if (i + reverse(i) === num) return true;
    }
    return false;
};