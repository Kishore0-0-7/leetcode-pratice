#include <stdio.h>
#include <stdlib.h>

char* fractionToDecimal(int numerator, int denominator) {
    if (numerator == 0) return "0";
    
    char* result = (char*)malloc(104 * sizeof(char));
    int index = 0;
    
    if ((numerator > 0) ^ (denominator > 0)) {
        result[index++] = '-';
    }
    
    long num = labs(numerator);
    long den = labs(denominator);
    
    long integerPart = num / den;
    sprintf(result + index, "%ld", integerPart);
    index += sprintf(result + index, "%ld", integerPart);
    
    long remainder = num % den;
    if (remainder == 0) {
        return result;
    }
    
    result[index++] = '.';
    
    int hashmap[10000] = {0};
    int pos = 0;
    
    while (remainder != 0) {
        if (hashmap[remainder] != 0) {
            int start = hashmap[remainder];
            int len = index - start;
            memmove(result + start + 1, result + start, len);
            sprintf(result + start, "(%.*s)", len, result + start + 1);
            return result;
        }
        
        hashmap[remainder] = index;
        remainder *= 10;
        sprintf(result + index, "%ld", remainder / den);
        index += sprintf(result + index, "%ld", remainder / den);
        remainder %= den;
    }
    
    return result;
}