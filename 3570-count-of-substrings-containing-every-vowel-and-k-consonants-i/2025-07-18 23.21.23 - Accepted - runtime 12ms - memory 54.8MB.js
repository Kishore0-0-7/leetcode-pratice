/**
 * @param {string} word
 * @param {number} k
 * @return {number}
 */
var countOfSubstrings = function(s, k) {
    let ans = 0;
    const n = s.length;

    for (let i = 0; i < n; i++) {
        let a = 0, e = 0, i_count = 0, o = 0, u = 0, c = 0;

        for (let j = i; j < n; j++) {
            const ch = s[j];
            if (ch === 'a') a++;
            else if (ch === 'e') e++;
            else if (ch === 'i') i_count++;
            else if (ch === 'o') o++;
            else if (ch === 'u') u++;
            else c++;

            if (a > 0 && e > 0 && i_count > 0 && o > 0 && u > 0 && c === k) {
                ans++;
            }
        }
    }

    return ans;
};