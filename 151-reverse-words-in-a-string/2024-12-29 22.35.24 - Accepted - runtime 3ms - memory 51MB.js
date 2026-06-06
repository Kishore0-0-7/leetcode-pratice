/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    const w = s.split(' ');
    const rw = w.reverse();
    return rw.filter(w => w.length > 0).join(' ');
};