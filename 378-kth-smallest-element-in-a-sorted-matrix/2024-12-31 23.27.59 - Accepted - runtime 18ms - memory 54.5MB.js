/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(matrix, k) {
    let lst = [];
        let n = matrix.length;
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                lst.push(matrix[i][j]);
            }
        }
        lst.sort((a, b) => a - b);
        return lst[k - 1];
};