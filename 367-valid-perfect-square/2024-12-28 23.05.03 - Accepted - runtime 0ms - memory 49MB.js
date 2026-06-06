var isPerfectSquare = function(num) {
    let a=0;
    a= Math.floor(Math.sqrt(num));
    return Math.pow(a,2) == num;
};