/**
 * @param {number[]} original
 * @param {number[][]} bounds
 * @return {number}
 */
var countArrays = function(original, bounds) {
    const n = original.length;
        let left = bounds[0][0];
        let right = bounds[0][1];

        for (let i = 1; i < n; i++) {
            const diff = original[i] - original[0];
            left = Math.max(left, bounds[i][0] - diff);
            right = Math.min(right, bounds[i][1] - diff);
        }

        return (left <= right) ? right - left + 1 : 0;
};