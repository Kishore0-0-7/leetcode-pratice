/**
 * @param {number[][]} nums1
 * @param {number[][]} nums2
 * @return {number[][]}
 */
var mergeArrays = function(nums1, nums2) {
    const map = new Map();
    for (const [i, v] of [...nums1, ...nums2]) {
        map.set(i, (map.get(i) || 0) + v);
    }
    return [...map.entries()].sort((a, b) => a[0] - b[0]);
};