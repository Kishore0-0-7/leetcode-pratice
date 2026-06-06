int countCompleteDayPairs(int* hours, int hoursSize) {
    int count = 0;
        int n = hoursSize;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if ((hours[i] + hours[j]) % 24 == 0) {
                    ++count;
                }
            }
        }
        return count;
}