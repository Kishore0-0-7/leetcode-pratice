/**
 * @param {number} n
 * @return {boolean}
 */
var canAliceWin = function(n) {
    let m=10;
    let t=0;
    while(n>=m){
        n-=m;
        m-=1;
        t=1-t;
    }
    return t!=0;
};