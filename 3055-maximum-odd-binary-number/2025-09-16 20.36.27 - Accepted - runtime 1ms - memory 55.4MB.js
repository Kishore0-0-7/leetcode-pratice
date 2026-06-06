/**
 * @param {string} s
 * @return {string}
 */
var maximumOddBinaryNumber = function(s) {
    let arr = s.split("");
    let ones = 0;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === "1") {
            arr[i] = "0";
            ones++;
        }
    }
    for (let i = 0; i < ones - 1; i++) {
        arr[i] = "1";
    }
    arr[arr.length - 1] = "1";
    return arr.join("");
};