/**
 * @param {number[][]} rectangles
 * @return {number}
 */
var countGoodRectangles = function(rectangles) {
    let count = 0;
  let squares = rectangles.map((item) => Math.min(...item));
  let maxLen = Math.max(...squares);
  for (let num of squares) {
    if (maxLen === num) count++;
  }
  return count;
};