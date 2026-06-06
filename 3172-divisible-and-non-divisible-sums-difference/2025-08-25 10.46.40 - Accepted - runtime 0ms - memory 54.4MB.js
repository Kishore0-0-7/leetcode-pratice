/**
 * @param {number} n
 * @param {number} m
 * @return {number}
 */
var differenceOfSums = function(n, m) {
    let div=0,nondiv=0;
        for(let i=1;i<n+1;i++)
            i%m==0?(div+=i):(nondiv+=i);
        return nondiv-div;
};