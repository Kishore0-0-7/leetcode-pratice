/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} x
 * @return {number[]}
 */
var findClosestElements = function(arr, k, x) {
    arr.sort((a, b) => {
      const diffA = Math.abs(a - x);
      const diffB = Math.abs(b - x);
      if (diffA === diffB) {
        return a - b;
      }
      return diffA - diffB;
    });
    const result = arr.slice(0, k).sort((a, b) => a - b);
    return result;
};