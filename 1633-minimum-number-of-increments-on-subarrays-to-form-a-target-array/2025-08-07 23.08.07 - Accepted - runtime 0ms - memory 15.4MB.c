int minNumberOperations(int* target, int targetSize) {
    int res = target[0];
        for (int i = 1; i < targetSize; ++i)
            res += (target[i] - target[i - 1])>0?target[i] - target[i - 1]: 0;
        return res;
}