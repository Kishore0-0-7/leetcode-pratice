var sortArrayByParity = function(nums) {
    let e = [];
    let o = [];
    for (let i of nums) {
        if (i % 2 === 0) {
            e.push(i);
        } else {
            o.push(i);
        }
    }
    return e.concat(o);
};