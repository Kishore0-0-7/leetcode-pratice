/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findPeaks(int* mountain, int mountainSize, int* returnSize) {
    int* peaks = (int*)malloc(mountainSize * sizeof(int)); // worst case: all peaks
    int count = 0;

    for (int i = 1; i < mountainSize - 1; i++) {
        if (mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1]) {
            peaks[count++] = i;
        }
    }

    *returnSize = count;
    return peaks;
}