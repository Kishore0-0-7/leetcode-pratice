/**
 * @param {string} s
 * @return {number}
 */
var minimumDeletions = function(s) {
    let res = 0;
    let count = 0;

    for (let i = 0; i < s.length; i++) {
        let c = s[i];
        if (c === 'b') {
            count++;
        } else if (count !== 0) {
            res++;
            count--;
        }
    }

    return res;
};