int countPrimes(int n) {

        if (n <= 2) {
            return 0;
        }
        
        int count = 1;
        for (int i = 3; i < n; i += 2) {
            bool isPrime = true;
            for (int j = 3; j * j <= i; j += 2) { 
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
    }
