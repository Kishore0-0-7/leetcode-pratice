/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 */
var compareVersion = function(version1, version2) {
    const v1 = version1.split(".");
    const v2 = version2.split(".");
    const length = Math.max(v1.length, v2.length);
    for (let i = 0; i < length; i++) {
        const v1_val = i < v1.length ? parseInt(v1[i]) : 0;
        const v2_val = i < v2.length ? parseInt(v2[i]) : 0;
        if (v1_val > v2_val) {
            return 1;
        }
        if (v1_val < v2_val) {
            return -1;
        }
    }
    return 0;
};