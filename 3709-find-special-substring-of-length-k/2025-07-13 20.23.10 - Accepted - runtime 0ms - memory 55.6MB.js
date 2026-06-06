/**
 * @param {string} s
 * @param {number} k
 * @return {boolean}
 */
var hasSpecialSubstring = function(s, k) {
    if (k >= s.length) {
        return s === s[0].repeat(k);
    }

    let i = 0;
    while (i < s.length) {
        let current = s[i];
        let j = i + 1;
        while (j < s.length && s[j] === current) {
            j++;
        }
        let length = j - i;
        if (length === k) {
            return true;
        }
        i = j;
    }
    return false;
};