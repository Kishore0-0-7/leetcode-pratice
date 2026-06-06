/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    if (n <= 2) {
            return 0;
        }
        
        var count = 1;
        for ( i = 3; i < n; i += 2) {
            let isPrime = true;
            for ( j = 3; j * j <= i; j += 2) { 
                if (i % j == 0) {
                    isPrime = false; 
                    break;
                }
            }
            if (isPrime) {
                count++;
            }
        }
        return count;
};