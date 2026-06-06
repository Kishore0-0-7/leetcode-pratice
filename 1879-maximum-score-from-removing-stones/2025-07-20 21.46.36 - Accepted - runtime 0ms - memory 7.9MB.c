int maximumScore(int a, int b, int c) {
    int total = a + b + c;
    int max = a > b ? (a > c ? a : c) : (b > c ? b : c);
    int half = total / 2;
    int result = half < (total - max) ? half : (total - max);
    return result;
}