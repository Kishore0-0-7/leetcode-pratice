/**
 * @param {number[]} nums
 * @return {number}
 */
var mostFrequentEven = function(nums) {
    const seen = {};
        for (const item of nums) {
            if (item % 2 === 0) {
                seen[item] = (seen[item] || 0) + 1;
            }
        }

        let maxCount = 0;
        let output = -1;

        for (const [numStr, count] of Object.entries(seen)) {
            const num = parseInt(numStr);
            if (count > maxCount) {
                maxCount = count;
                output = num;
            } else if (count === maxCount) {
                output = Math.min(output, num);
            }
        }

        return output;
};