/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal=function(triangle) {
    for (let i=triangle.length - 2; i >= 0; i--) {
        for (let j=0; j < triangle[i].length; j++) {
            let down=triangle[i + 1][j];
            let diag=triangle[i + 1][j + 1];
            triangle[i][j] += Math.min(down, diag);
        }
    }
    return triangle[0][0];
};