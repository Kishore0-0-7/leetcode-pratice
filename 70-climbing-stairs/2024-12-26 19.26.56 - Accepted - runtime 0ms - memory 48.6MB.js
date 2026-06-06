/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    if(n<=2)
        return n;
        let x=1,y=2,z=0;
        for (i=2;i<n;i++){
            z=x+y;
            x=y;
            y=z;
        }
        return z;
};