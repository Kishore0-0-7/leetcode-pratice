int secondHighest(char* s) {
    int seen[10]={0};
    for (int i=0;s[i]!='\0';i++) {
        if (isdigit(s[i])) {
            seen[s[i]-'0']=1;
        }
    }
    int count=0;
    for (int i=9;i>=0;i--) {
        if (seen[i]) {
            count++;
            if (count==2) return i;
        }
    }
    return -1;
}