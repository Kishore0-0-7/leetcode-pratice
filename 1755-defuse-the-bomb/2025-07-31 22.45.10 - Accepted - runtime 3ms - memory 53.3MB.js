/**
 * @param {number[]} code
 * @param {number} k
 * @return {number[]}
 */
var decrypt = function(code, k) {
    const n = code.length;
    const result = [];

    for (let i = 0; i < n; i++) {
        let total = 0;
        if (k > 0) {
            for (let j = 1; j <= k; j++) {
                total += code[(i + j) % n];
            }
        } else if (k < 0) {
            for (let j = 1; j <= -k; j++) {
                total += code[(i - j + n) % n];
            }
        }
        result.push(total);
    }

    return result;
};