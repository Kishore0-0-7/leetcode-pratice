int removePalindromeSub(char* s) {
    int len = strlen(s);
    if(len==0) return 0;
        char rev[len+1];
        for(int i=0;i<len;i++) rev[i]=s[len-i-1];
        rev[len]='\0';
        if (strcmp(s,rev)==0) return 1;
        else return 2;
}