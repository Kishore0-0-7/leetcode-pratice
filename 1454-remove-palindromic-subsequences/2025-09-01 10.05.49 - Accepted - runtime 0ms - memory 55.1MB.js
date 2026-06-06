/**
 * @param {string} s
 * @return {number}
 */
var removePalindromeSub = function(s) {
    if (s==="") return 0;
    let rev=s.split("").reverse().join("");
    if (s==rev) return 1;
    else return 2;
};