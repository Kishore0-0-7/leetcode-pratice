/**
 * @param {string} s
 * @return {number}
 */
var secondHighest = function(s) {
    let setDigits = new Set();
    for (let c of s) {
        if (/\d/.test(c)) {
            setDigits.add(Number(c));
        }
    }
    let nums=Array.from(setDigits).sort((a, b)=>a-b);
    if (nums.length<=1) return -1;
    return nums[nums.length-2];
};