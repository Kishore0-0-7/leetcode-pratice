/**
 * @param {string[]} list1
 * @param {string[]} list2
 * @return {string[]}
 */
var findRestaurant = function(list1, list2) {
    const list2Map = new Map();
    
    for(let i = 0; i < list2.length; i++){
        list2Map.set(list2[i], i);
    }
    
    let minIdxSum = 9999;
    let result = [];
    for(let i = 0; i < list1.length; i++){
        let idx = list2Map.get(list1[i]);
        if(idx !== undefined){
            let idxSum = idx + i;
            if(idxSum < minIdxSum){
                minIdxSum = idxSum;
                result = [list1[i]];
            }
            else if(idxSum === minIdxSum)
                result.push(list1[i]);
        }
    }

    return result;
};