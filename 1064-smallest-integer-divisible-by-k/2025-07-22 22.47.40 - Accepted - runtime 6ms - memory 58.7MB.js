/**
 * @param {number} k
 * @return {number}
 */
var smallestRepunitDivByK = function(k) {
    if (![1, 3, 7, 9].includes(k % 10)) return -1;
        let mod = 0;
        const modSet = new Set();
        for (let length = 1; length <= k; length++) {
            mod = (10 * mod + 1) % k;
            if (mod === 0) return length;
            if (modSet.has(mod)) return -1;
            modSet.add(mod);
        }
        return -1;
};