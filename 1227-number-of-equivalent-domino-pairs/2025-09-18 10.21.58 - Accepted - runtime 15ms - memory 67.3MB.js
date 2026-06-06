/**
*@param {number[][]} dominoes
*@return {number}
 */
var numEquivDominoPairs=function(dominoes) {
    let mp=new Map();
    let count=0;
    for (let [a, b] of dominoes) {
        let key=Math.min(a, b)*10+Math.max(a, b); 
        count+=mp.get(key) || 0;
        mp.set(key,(mp.get(key)||0)+1);
    }
    return count;
};