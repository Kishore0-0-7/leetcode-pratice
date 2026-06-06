/**
 * @param {string} num
 * @return {boolean}
 */
var digitCount = function(num) {
  for (let i = 0; i < num.length; i++) {
        let digit = parseInt(num[i]);
        let count = 0;
        for (let j = 0; j < num.length; j++) {
            if (parseInt(num[j]) === i) {
                count++;
            }
        }
        if (digit !== count) {
            return false;
        }
    }
    return true;  
};