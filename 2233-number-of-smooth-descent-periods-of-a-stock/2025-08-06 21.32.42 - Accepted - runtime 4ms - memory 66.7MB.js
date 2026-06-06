/**
 * @param {number[]} prices
 * @return {number}
 */
var getDescentPeriods = function(prices) {
    let l = 0;
    let ans = 0;
    for (let r = 0; r < prices.length; r++) {
        if (r > 0 && prices[r] !== prices[r - 1] - 1) {
            l = r;
        }
        ans += (r - l + 1);
    }
    return ans;
};