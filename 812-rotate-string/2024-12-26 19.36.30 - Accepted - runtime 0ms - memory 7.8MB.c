bool rotateString(char* s, char* goal) {
    if(strlen(s) != strlen(goal)) return false;
    char d[2 * strlen(s) + 1];
    strcpy(d, s);
    strcat(d, s);
    return strstr(d, goal) != NULL;
}