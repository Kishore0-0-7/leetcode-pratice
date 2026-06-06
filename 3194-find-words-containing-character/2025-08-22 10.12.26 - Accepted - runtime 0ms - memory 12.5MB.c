/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findWordsContaining(char** words, int wordsSize, char x, int* returnSize) {
    int* list = (int*)malloc(wordsSize * sizeof(int));
    int count = 0;
    for (int i = 0; i < wordsSize; i++) {
        if (strchr(words[i], x) != NULL) {
            list[count++] = i;
        }
    }
    *returnSize = count; // set output size
    return list;  
}