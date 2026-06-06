/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let lst=[]
    for(let i=0;i<arr.length;i++){
        if(fn(arr[i],i))
        lst.push(arr[i]);
    }
    return lst;
};