class Solution {
    public int findMinFibonacciNumbers(int k) {
        List<Integer> fib = new ArrayList<>();
        fib.add(1);
        fib.add(1);

        while (fib.get(fib.size() - 1) < k) {
            int n = fib.size();
            fib.add(fib.get(n - 1) + fib.get(n - 2));
        }

        int count = 0;
        for (int i = fib.size() - 1; i >= 0; i--) {
            if (k >= fib.get(i)) {
                k -= fib.get(i);
                count++;
            }
            if (k == 0) break;
        }

        return count;
    }
}