/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    let ns={};
    for(let i=0;i<numbers.length;i++){
        let t=target-numbers[i];
        if (t in ns)
        return [ns[t]+1,i+1];
        ns[numbers[i]]=i;
    }
    return []
};