var fib = function(n) {
    if (n<=1) return n

        let a=0, b = 1;
        for (let i=2;i<n;i++){
            let t=b;
            b = a+b;
            a=b;
        }
        return b;
};