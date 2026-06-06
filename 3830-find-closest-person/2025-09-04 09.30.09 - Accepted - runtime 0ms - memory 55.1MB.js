/**
 * @param {number} x
 * @param {number} y
 * @param {number} z
 * @return {number}
 */
var findClosest = function(x, y, z) {
    let l1=Math.abs(x-z);
        let l2=Math.abs(y-z);
        if(l1>l2)
            return 2;
        else if(l1<l2)
            return 1;
        return 0;
};