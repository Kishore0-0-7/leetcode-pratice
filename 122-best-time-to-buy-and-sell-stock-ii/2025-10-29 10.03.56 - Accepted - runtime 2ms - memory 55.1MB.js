/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let start=prices[0],m=0;
        for(let i=1;i<prices.length;i++){
            if(start<prices[i]) m+=prices[i]-start;
            start=prices[i];
        }
        return m;
};